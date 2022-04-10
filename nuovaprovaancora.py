#Import all important functionality
import cv2
import mediapipe as mp
from Alarm import Alarm
""" import SendSmsForRaspberryPi
from SendSmsForRaspberryPi import SendSms1
from SendSmsForRaspberryPi import SendSms2

from datetime import datetime
import serial as io
 """ 

#Start cv2 video capturing through CSI port
cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose(model_complexity
= 1, min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

#Inizializzare la comunicazione
""" now = datetime.now()
current_time = now.strftime("%H:%M:%S")
gsm = io.Serial("/dev/ttyUSB0",9600, timeout=0.5)
gsm.flush()
 """



#Start endless loop to create video frame by frame Add details about video size and image post-processing to better identify bodies
def FallDetection():
    # Parte la falldetection vera e propria
    #while (len(BaricentroStory) < 1000 and count < 1) : # fai 1000 tentativi di rilevamento poi reinizializza l'array 
    ret,frame=cap.read()
    flipped=cv2.flip(frame,flipCode= 1)
    frame1 = cv2.resize(flipped,(640,480))
    rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    result=pose.process(rgb_img)
    mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("frame",rgb_img)
    key = cv2.waitKey(1) & 0xFF
    BaricentroStory = [] # inizializzazione storico dei valori del baricentro
    Differenza = 0
    #if key ==ord("q"):
    #    break
    #print('X Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640)
    while len(BaricentroStory) < 500:
        print(len(BaricentroStory))
        #while True:
            
        try:
            x = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * 480
            y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * 480
            z = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480
            ret,frame=cap.read()
            flipped=cv2.flip(frame,flipCode= 1)
            frame1 = cv2.resize(flipped,(640,480))
            rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
            result=pose.process(rgb_img)
            mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
            cv2.imshow("frame",rgb_img)
            key = cv2.waitKey(1) & 0xFF
            if(((result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].visibility) > 0.8)
            and ((result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].visibility) > 0.8)
            and ((result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].visibility) > 0.8)):
                print('Rilevamento in corso!')
                Baricentro = (x+y+z)/3
                BaricentroStory.append(Baricentro)
                #print(BaricentroStory)
                #if BaricentroStory[-2]!=0:
                Differenza = (BaricentroStory[-2] - BaricentroStory[-1])
                print('la differenza è', Differenza)    
                if Differenza < -40:
                    return Alarm() 
                else: 
                    continue    

            else:
                print('Per favore rientra nell\' inquadratura!')
        
        except:
            print('Visibilità non sufficiente!')
            break
            
    FallDetection() # Se dopo 500 iterazioni della rilevazione non c'è stata una caduta allora reinizializza la lista BaricentroStory[] e ricomincia 
            
        

 
            
if __name__ == "__main__":
    FallDetection()
        
            

        
            
