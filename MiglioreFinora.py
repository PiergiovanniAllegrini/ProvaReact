import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()

y1 = [0, 0] # inizializzazione coordinata verticale naso
frame = 0
y = 0

def FallDetection():
        success, img = cap.read()
        img = detector.findPose(img) # prende una prima posa
        count = -1 # numero di cadute rilevate
        lmList = detector.findPosition(img, draw = False)   # se non c'è abbastanza visibilità lo dice già da qui        
        while count < 1:
                try:
                    success, img = cap.read()
                    img = detector.findPose(img) # prende una prima posa
                    lmList = detector.findPosition(img, draw = False) # costruisce la lista dei landmarks
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
    
        

