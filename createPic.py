#!/usr/bin/env python
import cv2
import numpy as np

videoname="201708311626320"
vc=cv2.VideoCapture(videoname+".ts")
#vc=cv2.VideoCapture("201708231458510.ts")
#vc=cv2.VideoCapture("201708311626320.ts")
#vc=cv2.VideoCapture("hand.flv")
#vc=cv2.VideoCapture('ILSVRC2015_train_00755001.mp4')
c=0

if vc.isOpened():
    rval,frame=vc.read()
    #print (1)
else:
    rval=False
    #print (0)
while rval:
    while (c+10)%10!=0:
        c=c+1    
        rval,frame=vc.read()
    if rval==False:
        print "ending of video"
        break;
    roi=frame[27:1052,22:865]
    cname=videoname+'_'+("%06d" % c)
    cv2.imwrite(videoname+'/'+cname+'.jpg',roi)
    print "save:"+str(c)
    c=c+1
    rval,frame=vc.read()
    #if c==1:
    #    rval=False
    #    break
    #cv2.waitKey(1)
vc.release()



