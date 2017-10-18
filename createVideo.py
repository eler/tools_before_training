# -*- coding: utf-8 -*-

#=================
#File: PyOpenCV.py
#Author: Wendy
#Date: 2013-12-03
#=================

#eclipse, python2.7, opencv 2.4.6

import cv2

#获得视频的格式
videoCapture = cv2.VideoCapture('201708311626320.ts')

#获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
size2 = (843,1025)
#指定写视频的格式, I420-avi, MJPG-mp4
#videoWriter = cv2.VideoWriter('201708311626320.mp4', cv2.FOURCC('M', 'J', 'P', 'G'), fps, size)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('201708311626320.mp4', fourcc, fps, size2)

#读帧
success, frame = videoCapture.read()
i = 0
while success :
#    cv2.imshow("Oto Video", frame) #显示
#    cv2.waitKey(1000/int(fps)) #延迟
    roi = frame[27:1052,22:865]
    videoWriter.write(roi) #写视频帧
    i = i + 1
    print i
    success, frame = videoCapture.read() #
