import cv2
import numpy as np
ListTxtPath = 'parking005/JPEGImages/list.txt'
picFilePath = 'parking005/JPEGImages/'
listTxt = open(ListTxtPath,'r')
mean = [0,0,0]
count = 0
while 1:
    onePicLine = listTxt.readline()
    imgName = picFilePath+onePicLine
    imgName = imgName.strip('\n')
    img = cv2.imread(imgName)
#    print imgName
#    print img.shape
#    mean = np.mean(img[:,:,0])

    mean = mean + np.array([np.mean(img[:,:,0]),np.mean(img[:,:,1]),np.mean(img[:,:,2])])/np.array([4109.0,4109.0,4109.0])
    count = count + 1
    print count,':',mean
print mean    
