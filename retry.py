import cv2
import mediapipe as mp
from Alarm import Alarm

cap=cv2.VideoCapture(0)

#Initialise Media Pipe Pose features
mp_pose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mp_pose.Pose(model_complexity
= 1, min_detection_confidence=0.7,
    min_tracking_confidence=0.7)


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



def Retry():

    for i in range(500):
            print(i)
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
                    Retry()    

            else:
                print('Visibilità non sufficiente per questa modalità!')
        
           