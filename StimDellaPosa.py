#Import all important functionality
import cv2
import mediapipe as mp

#Start cv2 video capturing through CSI port
cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose()

#Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
def FallDetection():
    while True:
        ret,frame=cap.read()
        flipped=cv2.flip(frame,flipCode=-1)
        frame1 = cv2.resize(flipped,(640,480))
        rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
        cv2.imshow("Image", rgb_img)
        result=pose.process(rgb_img)
        # Parte la falldetection vera e propria
        count = -1 # numero di cadute rilevate
        while count < 1:
            y = 0
            y1 = [] # inizializzazione coordinata verticale naso
            while len(y1) < 6:
             try:
               print(len(y1))
               mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
               cv2.imshow("Image", rgb_img)
               #print('Rilevamento in corso!')
               #print('X Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640)
               #print('Y Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480)
               y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480   # coordinata verticale del naso
               y1.append(y)   # memorizza valore di y del naso per confontarlo
               print(y1)  # QUI BISOGNA RISOLVERE Y1 CHE CRESCE INDETERMINATAMENTE
               cv2.waitKey(1)
               if ((y1[-1] - y1[-2]) > 1):  # è la distanza verticale del naso da un frame all'altro e viene comparata con un valore di soglia (se il naso si è spostato più della soglia da un solo frame all'altro, vuol dire che la persona è caduta) 
                 #if result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z= 0.8:         # se la visibilità è maggiore della soglia di 0.8 la caduta è valida. Metto il comando dopo la soglia per controllare che non si tratti solo di un'uscita dall'inquadratura
                 count+=1
               else:
                  counter+=1
             except:
              print('Visibilità non sufficiente')
              FallDetection()
            FallDetection()
        print('Caduta rilevata, allarme!')
        cv2.putText(rgb_img, "Caduta rilevata", (20,50), cv2.FONT_HERSHEY_COMPLEX, 2.5, (0,0,255), 
                   2, 11)
        print('Inizio la richiesta di aiuto!')
    
        

            


if __name__ == "__main__":
    FallDetection()
