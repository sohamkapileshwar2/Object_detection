import sys
import os
import cv2
import matplotlib.pyplot as plt


os.chdir('D:\documents\darkflow\darkflow-master')
# print(os.getcwd())
# print(sys.path)

sys.path.append('D:\documents\darkflow\darkflow-master')

from darkflow.net.build import TFNet


options = {
    'model':'cfg\\tiny-yolo-coco-3c.cfg',
    'load': 2125,
    'threshold': 0 ,
    'gpu': 1.0
}

tfnet = TFNet(options)

img = cv2.imread('cars_image.jpg')
print(img.shape)

result = tfnet.return_predict(img)
print(result)

img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)

for i in range(len(result)):
    tl = (result[i]['topleft']['x'],result[i]['topleft']['y'])
    br = (result[i]['bottomright']['x'],result[i]['bottomright']['y'])
    label = result[i]['label']
    img = cv2.rectangle(img,tl,br,(0,255,0),2)
    img = cv2.putText(img,label,(tl[0] , tl[1] - 5) , cv2.FONT_HERSHEY_COMPLEX,0.3, (255,255,155),1)


plt.figure(figsize = (10,10))
plt.imshow(img)
plt.show()
