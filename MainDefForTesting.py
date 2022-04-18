#Import all important functionality
import time
from tkinter import W
import cv2
import mediapipe as mp
from Alarm import Alarm
import numpy as np
""" import SendSmsForRaspberryPi
from SendSmsForRaspberryPi import SendSms1
from SendSmsForRaspberryPi import SendSms2

from datetime import datetime
import serial as io
 """ 
#Start cv2 video capturing through CSI port
for i in range(49,71,1):
    cap=cv2.VideoCapture("C:/Users/Piergiovanni/Desktop/FallDataset/Coffee_room_02/Coffee_room_02/Videos/video (%d).avi"%i)
    #Initialise Media Pipe Pose features
    mp_pose=mp.solutions.pose
    mpDraw=mp.solutions.drawing_utils
    pose=mp_pose.Pose(model_complexity
    = 1, min_detection_confidence=0.9,
        min_tracking_confidence=0.9)

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
        try:
            ret,frame=cap.read()
            flipped=cv2.flip(frame,flipCode= 1)
            frame1 = cv2.resize(flipped,(640,480))
            rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB) # Mediapipe lavora in RGB e opencv in BGR
            result=pose.process(rgb_img)
            mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
            cv2.imshow("frame",rgb_img)
            key = cv2.waitKey(1) & 0xFF
            BaricentroStory = [0,0] # inizializzazione storico dei valori del baricentro
            Differenza = 0
            #if key ==ord("q"):
            #    break
            #print('X Coords are', result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * 640)
                #print(j)
            while True:
                
                try:
                    start = time.time()
                    x = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * 480
                    y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * 480
                    z = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480
                    
                    """ w = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].z 
                    t = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].z 
                    k = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z 
                    """
                    ret,frame=cap.read()
                    flipped=cv2.flip(frame,flipCode= 1)
                    frame1 = cv2.resize(flipped,(640,480))
                    rgb_img=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
                    result=pose.process(rgb_img)
                    mpDraw.draw_landmarks(rgb_img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
                    cv2.imshow("frame",rgb_img)
                    key = cv2.waitKey(1) & 0xFF
                    if(((result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].visibility) > 0.9)
                    and ((result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].visibility) > 0.9)
                    and ((result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].visibility) > 0.9)):
                        #print('Rilevamento in corso!')
                        BaricentroOrdinata = (x+y+z)/3
                        #BaricentroProfondità = k
                        BaricentroStory.append(BaricentroOrdinata)
                        #print(BaricentroStory)
                        #if BaricentroStory[-2]!=0:
                        #print('lo storico del baricentro è', BaricentroStory)
                        Differenza = (BaricentroStory[-2] - BaricentroStory[-1])
                        
                        print("il baricentro è " , BaricentroOrdinata)
                        print('la differenza è', Differenza)
                        
                        #print('la media degli ultimi 100 valori del baricentro è', np.mean(BaricentroStory[-100:-1]))    
                        #print('la profondità del baricentro è', BaricentroProfondità)
                    
                        if Differenza < -10 and len(BaricentroStory) > 60:  
                            Risultati= open("Risultati2TestCoffee_room_02.txt", "a")
                            Risultati.write("\nCaduta rilevata nel video numero %d"%i)
                            Risultati.close()
                            return Alarm()
                        elif len(BaricentroStory) > 150 and np.mean(BaricentroStory[-150:-1]) > 300: 
                            Risultati= open("Risultati2TestCoffee_room_02.txt", "a")
                            Risultati.write("\nCaduta rilevata nel video numero %d"%i)
                            Risultati.close()
                            return Alarm()
                        elif len(BaricentroStory) == 500000:
                            BaricentroStory = []
                            print('RESET RESET RESET RESET RESET')  
                        else: 
                            end = time.time()
                            totalTime = end - start
                            fps = 1 / totalTime
                            print("FPS: ", fps)
                            #print(i)
                            continue    

                    else:
                        print('Imposibile rilevare la figura intera!')
                        BaricentroStory = []
                except:
                    print('Visibilità non sufficiente!')
                    break
        except:
            Risultati= open("Risultati2TestCoffee_room_02.txt", "a")
            Risultati.write("\nNessuna caduta rilevata nel video numero %d"%i)
            Risultati.close()
            return 1
        
                        
        FallDetection() # Dopo 500 iterazioni senza rilevazione di alcun corpo resetta FallDetection                
            

    
                


    if __name__ == "__main__":
        FallDetection()
            
                

            
                
                            
