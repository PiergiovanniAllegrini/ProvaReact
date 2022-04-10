import cv2
import mediapipe as mp
import time




x = result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * 480
y = result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * 480
z = result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * 480
        


def Rilevamento():
    print('Rilevamento in corso!')
    BaricentroStory.append(Baricentro)   # memorizza valore di y del naso per confontarlo
    print(BaricentroStory)
    #print('il conto cadute è ' , count)
    Differenza = (BaricentroStory[-2] - BaricentroStory[-1])
    if (Differenza > 200):  # è la distanza verticale del naso da un frame all'altro e viene comparata con un valore di soglia (se il naso si è spostato più della soglia da un solo frame all'altro, vuol dire che la persona è caduta)     
        print('la differenza è', Differenza)
        print('il conto cadute è ' , count)    
        count +=1