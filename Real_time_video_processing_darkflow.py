import sys
# #print(sys.path)
# sys.path.remove('C:\\Users\\soham\\AppData\\Roaming\\Python\\Python37\\site-packages')
# #print('\n')
# #print(sys.path)



import cv2
import numpy as np
import time
import os

# print(os.getcwd())
os.chdir('D:\documents\darkflow\darkflow-master')
sys.path.append('D:\documents\darkflow\darkflow-master')

from darkflow.net.build import TFNet



print('\n')
print(cv2.__file__)
print(cv2.__version__)




options = {
    'model':'cfg\\tiny-yolo-coco-3c.cfg',
    'load': 2125,
    'threshold':0 ,
    'gpu':1.0
}


tfnet = TFNet(options)

capture = cv2.VideoCapture('D:\documents\darkflow\darkflow-master\hitman_agent_47.mp4')
colors = [tuple(255*np.random.rand(3)) for i in range(5)]

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
while(capture.isOpened()):
    stime = time.time()
    ret , frame = capture.read()
    results = tfnet.return_predict(frame)
    if ret:
        for color,result in zip(colors,results):
            tl = (result['topleft']['x'] , result['topleft']['y'])
            br = (result['bottomright']['x'] , result['bottomright']['y'])
            label = result['label']
            conf = result['confidence']
            frame = cv2.rectangle(frame,tl,br,color,2)
            frame = cv2.putText(frame,label + '(' + str(conf) + ')',tl,cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        cv2.imshow('video',frame)
        print('FPS : {}'.format(1 / (time.time()- stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
