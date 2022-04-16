import time


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
    #SendSms1("Emergenza in corso, per favore controlla che sia tutto a posto " + current_time)
    #SendSms2("Emergenza in corso, per favore controlla che sia tutto a posto " + current_time)
    time.sleep(5)    
    