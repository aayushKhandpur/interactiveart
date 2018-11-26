import cv2
from matplotlib import pyplot as plt

fgbg = cv2.createBackgroundSubtractorMOG2()
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv2.imshow("orig", frame)
    fgmask = fgbg.apply(frame)
    mask_rgb = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2RGB)
    out_frame = cv2.bitwise_and(frame, mask_rgb)
    grey = cv2.cvtColor(out_frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.imshow("FG", thresh)
    _, contours, _ = cv2.findContours(grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = contours[0]
    print grey.shape
    print(cnts)
    cv2.drawContours(frame, cnts, -1, (0, 0, 255), 5)
    #cv2.imshow('fgmask',frame)
    #cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()