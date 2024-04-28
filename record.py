import cv2
from datetime import datetime
from cv2 import VideoCapture
from cv2 import waitKey
from time import strftime

def record():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    storage =cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi',fourcc,20.0,(640,480))

    while True :
        ret,frame=cap.read()
        cv2.putText(frame,f'{datetime.now(),strftime("%D-%H-%M-%S")}',(50,50),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,255),2)
        
        storage.write(frame)


        cv2.imshow('esc to stop',frame)

        if cv2.waitKey(1)==27:
           cap.release()
           cv2.destroyAllWindows()
           
           break
        