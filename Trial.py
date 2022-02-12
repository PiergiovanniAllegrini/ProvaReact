import cv2
import mediapipe as mp
import time


cap=cv2.VideoCapture(0)
pTime = 0

y1 = [0, 0] # inizializzazione coordinata verticale naso
frame = 0
y = 0

mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose()


def findPose(img, draw=True): 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        if results.pose_landmarks:
            if draw:
                mpDraw.draw_landmarks(img, results.pose_landmarks,
                                           mpPose.POSE_CONNECTIONS)
        return img
    
def findPosition(img, draw=True):
    lmList = []
    if results.pose_landmarks:
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape  # height, width, channel
                #print(id, lm)
                cx, cy, visibility = int(lm.x * w), int(lm.y * h), lm.visibility # ho moltiplicato la x per la larghezza per ottenere l'esatta coordinata poiché x darebbe la coordinata normalizzata, stessa cosa per y
                lmList.append([id, cx, cy, visibility])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
                return lmList
    else:
        print('Visibilità non sufficiente')
                

"""while True:
    ret,frame=cap.read()
    flipped=cv2.flip(frame,flipCode=-1)
    frame1 = cv2.resize(flipped,(640,480))
    rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    result=pose.process(rgb_img)
    print (result.pose_landmarks)
    mpDraw.draw_landmarks(frame1,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("frame",frame1)
    
    key = cv2.waitKey(1) & 0xFF
    if key ==ord("q"):
        break
   """     


def FallDetection():
        success, img = cap.read()
        flipped=cv2.flip(img,flipCode=-1)
        frame1 = cv2.resize(flipped,(640,480))
        rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
        img = findPose(rgb_img) # prende una prima posa
        count = -1 # numero di cadute rilevate
        lmList = findPosition(img, draw = False)   # se non c'è abbastanza visibilità lo dice già da qui        
        print(count)
        while count < 1:
                try:
                    success, img = cap.read()
                    img = findPose(img) # prende una prima posa
                    lmList = findPosition(img, draw = False) # costruisce la lista dei landmarks
                    a = lmList[0]   # coordinate naso                
                    y = a[2]   # coordinata verticale del naso
                    y1.append(y)   # memorizza valore di y del naso per confontarlo
                    cv2.imshow("Image", img)
                    cv2.waitKey(1)
                    print('Rilevamento in corso!')
                    if ((y1[-1] - y1[-2]) > 20):  # è la distanza verticale del naso da un frame all'altro e viene comparata con un valore di soglia (se il naso si è spostato più della soglia da un solo frame all'altro, vuol dire che la persona è caduta) 
                        if a[3]>= 0.8:         # se la visibilità è maggiore della soglia di 0.8 la caduta è valida. Metto il comando dopo la soglia per controllare che non si tratti solo di un'uscita dall'inquadratura
                            count+=1
                    else:
                        FallDetection()
                except:
                    print('Visibilità non sufficiente')
                    FallDetection()
        
        """ cv2.imshow("Image", img) """
        print('Caduta rilevata, allarme!')
        cv2.putText(img, "Caduta rilevata", (20,50), cv2.FONT_HERSHEY_COMPLEX, 2.5, (0,0,255), 
                    2, 11)
        print('Inizio la richiesta di aiuto!')
        
                
                    
                
                

FallDetection()