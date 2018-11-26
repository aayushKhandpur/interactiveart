import cv2
import numpy as np
import time

fgbg = cv2.createBackgroundSubtractorMOG2()
cam = cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    #cv2.imshow('f',frame)
    frame = cv2.resize(frame, (8,6))
    h1=640/12
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(frame, (9, 9))
    frame=cv2.flip(frame,90)
    #cv2.imshow("f1", frame)
    mask = fgbg.apply(frame)
    maskb = mask
    mask = cv2.blur(mask, (4, 4))
    _, cont, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cont:
        continue
    contours = cont[0]
    area = cv2.contourArea(contours)  # divide the area into no. of parts required
    print(area)
    # for cnt in cont[0]:
    #     area = cv2.contourArea(cont[0])  # divide the area into no. of parts required
    #     print(area)