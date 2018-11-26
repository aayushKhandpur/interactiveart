import cv2, numpy as np
import serial, time
import struct
from skimage import measure
# check if serial is available
def isSerialAvailable():
    #input = ser.readline()
    print(input)
    return "OK" in input


def getGreyScaleFrame(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def imageProcess(baseFrame, currentFrame):
    resultdata = ""
    # images, ensuring that the difference image is returned
    (score, diff) = measure.compare_ssim(baseFrame, currentFrame, full=True, multichannel=True)
    diff = (diff * 255).astype("uint8")
    print(score)
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    threshArr = np.array(thresh)
    print threshArr
    if (abs(1 - score) < .15):
        return "000000000000000000000000000000000000000000000000"
       # return '111111110000111111110000000011111111000000001111'

    rows = threshArr.shape[0]
    cols = threshArr.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if (threshArr[x][y] > 0):
                resultdata += "1"
            else:
                resultdata += "0"

    return resultdata




# configure the serial connections (the parameters differs on the device you are connecting to)
#ser = serial.Serial('COM3', 9600, timeout=1)

# if ser.isOpen():
#     print(ser.name + ' is open...')

cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    cv2.imshow('base', frame)
    frame = cv2.resize(frame, (800, 600))
    frame = cv2.flip(frame , 1 )
    fgmask = fgbg.apply(frame)
    rows = fgmask.shape[0]
    cols = fgmask.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if(fgmask[x][y] > 127):
                print(x , y ,':', fgmask[x][y])
                pixel = (x+1) * (y+1)
                print pixel
             #   ser.write(struct.pack('>B',2))
    # if(fgmask[0][3] > 0):
    #     print(fgmask[0][3])
    #     ser.write(struct.pack('>B', 30))
    # else:
    #     print(fgmask[0][3])
    #     ser.write(struct.pack('>B', 0))



    cv2.imshow('frame',fgmask)
    time.sleep(.2)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
print fgmask
