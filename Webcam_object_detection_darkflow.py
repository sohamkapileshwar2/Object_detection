import os
import numpy as np
import cv2
import time

print(cv2.__file__)
print(cv2.__version__)
print('\n')

print(os.getcwd())
os.chdir('D:\documents\darkflow\darkflow-master')
print(os.getcwd())
print('\n')

from darkflow.net.build import TFNet

options = {
    'model': 'cfg\yolo.cfg',
    'load':'weights\yolov2.weights',
    'threshold':0.4,
    'gpu':1.0
}


tfnet = TFNet(options)

capture = cv2.VideoCapture(0)
cv2.namedWindow('webcam' , cv2.WINDOW_NORMAL)
while(capture.isOpened()):
    ret,frame = capture.read()
    if ret:
        stime = time.time()
        results = tfnet.return_predict(frame)
        for result in results:
            tl = (result['topleft']['x'],result['topleft']['y'])
            br = (result['bottomright']['x'],result['bottomright']['y'])
            label = result['label']
            conf = result['confidence']
            text = '{} : {:.3f}'.format(label,conf*100)
            frame = cv2.rectangle(frame,tl,br,(0,255,0),2)
            frame = cv2.putText(frame,text, (tl[0] - 5 , tl[1] - 5) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (255,255,255) , 1)
        cv2.imshow('webcam' , frame)
        print('FPS : {}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows








