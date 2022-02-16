#Import all important functionality
import cv2
import mediapipe as mp
import SendSmsForWindows
from SendSmsForWindows import SendSms1
from SendSmsForWindows import SendSms2
import time
from datetime import datetime
import serial as io


#Start cv2 video capturing through CSI port
cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose(model_complexity
= 1, min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

#Inizializzare la comunicazione
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
gsm = io.Serial("COM7",9600, timeout=0.5)
gsm.flush()




#Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
def FallDetection():
    # Parte la falldetection vera e propria
    X = 0
    y = 0
    y1 = [0,0] # inizializzazione coordinata verticale naso
    count = -1
    while (len(y1) < 1000 and count < 1) : # fai 1000 tentativi di rilevamento poi reinizializza l'array 
        ret,frame=cap.read()
        flipped=cv2.flip(frame,flipCode= 1)
        frame1 = cv2.resize(flipped,(640,480))
        rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
        result=pose.process(rgb_img)
        mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        cv2.imshow("frame",rgb_img)
        key = cv2.waitKey(1) & 0xFF
        if key ==ord("q"):
            break
        #print('X Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640)
        
            

        try:
            # Se si vuole modalità di rilevazione che usa i fianchi togliere il commento a "Left_Hip" e "Right_Hip"
            # Se si vuole modalità basata su accelerazioni togliere il commento a "Nose" e commentare "Left_Hip" e "Right_Hip"
            #x = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * 480
            #y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * 480
            y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480
            # print('Y Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480)
            
            y1.append(y)   # memorizza valore di y del naso per confontarlo
            if((result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].visibility)) > 0.8:
            #if((result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].visibility) > 0.8 or (result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].visibility) > 0.8):
                print('Rilevamento in corso!')
                if ((y1[-1] - y1[-2]) > 1):  # è la distanza verticale del naso da un frame all'altro e viene comparata con un valore di soglia (se il naso si è spostato più della soglia da un solo frame all'altro, vuol dire che la persona è caduta)     
            
            #if (x > 400 and y > 400):   
                    count +=1
                    print(' il conto cadute è ' , count)
                    if count == 1:
                        return Alarm()
            else:
                print('Visibilità non sufficiente per questa modalità!')
        except:
               print('Visibilità non sufficiente!')
               FallDetection()
            
    FallDetection() # Se dopo 10 iterazioni della rilevazione non c'è stata una caduta allora reinizializza la lista y1[] e ricomincia 
            
        


# Funzione di allarme
def Alarm():
    #ret,frame=cap.read()
    #flipped=cv2.flip(frame,flipCode=-1)
    #frame1 = cv2.resize(flipped,(640,480))
    #rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    print('Caduta rilevata, allarme!')
    #cv2.putText(rgb_img, "Caduta rilevata", (20,50), cv2.FONT_HERSHEY_COMPLEX, 2.5, (0,0,255), 
     #              2, 11)
    print('Inizio la richiesta di aiuto!')
    SendSms1("Emergenza in corso, per favore controlla che sia tutto a posto " + current_time)
    SendSms2("Emergenza in corso, per favore controlla che sia tutto a posto " + current_time)
        

            


if __name__ == "__main__":
    FallDetection()

