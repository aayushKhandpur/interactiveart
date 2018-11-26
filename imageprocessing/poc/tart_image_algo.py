import cv2, numpy as np
import serial, time
from skimage import measure

# check if serial is available
def isSerialAvailable():
    #input = ser.readline()
    print(input)
    return "OK" in input


def getGreyScaleFrame(frame):
    return cv2.cvtColor(frame, cv2.COLOR_RGB2HSV_FULL)


def imageProcess(baseFrame, currentFrame):
    resultdata = ""
    # images, ensuring that the difference image is returned
    (score, diff) = measure.compare_ssim(baseFrame, currentFrame, full=True, multichannel=True)
     #cv2.imshow('noiseframe', diff)
     #diff = cv2.fastNlMeansDenoisingMulti(diff, 0, 1,  None, 4, 7, 35)
    diff = (diff * 255).astype("uint8")
    print(score)
    #
    # # obtain the regions of the two input images that differ
    #thresh1 = cv2.threshold(diff, 0, 1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    thresh = cv2.threshold(diff, 100, 1, cv2.THRESH_BINARY_INV)[1]
    threshArr = np.array(thresh)
    print threshArr
    if (abs(1 - score) < .015):
         return "000000000000000000000000000000000000000000000000"
    #    # return '111111110000111111110000000011111111000000001111'

    rows = threshArr.shape[0]
    cols = threshArr.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            #resultdata.join((threshArr[x][y]))
             if (threshArr[x][y] > 0):
                 resultdata += "1"
             else:
                 resultdata += "0"

    return resultdata


# program starts here
#Connect to the serial port

ser = serial.Serial('COM1', 9600, timeout=10)
if ser.isOpen():
   print(ser.name + ' is open...')
frameCount = 0
#cap = cv2.VideoCapture('http://192.168.1.16:8080/video')
cap = cv2.VideoCapture(0)
while 1:
    start = time.time()
    frameCount += 1
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if frameCount < 100:
        continue
    frame = cv2.flip(cv2.resize(frame, (6, 8)),1)

    #cv2.imshow('frame', frame)
    #frame = cv2.flip(cv2.resize(cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21), (6, 8)),1)
    #frame = ((cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)).resize(frame, (6, 8))).flip(frame, 1)

    if frameCount == 100:
        baseFrame = getGreyScaleFrame(frame)
        #baseFrame = cv2.fastNlMeansDenoisingColored(baseFrame, None, 10, 10, 7, 21)
        print "Base frame selected"
        baseEnd = time.time()
        print(baseEnd - start)
        continue

    # convert the images to grayscale
    currentFrame = getGreyScaleFrame(frame)
    result = imageProcess(baseFrame, currentFrame)
    print result
    end = time.time()
    print(end - start)
    if result.__len__() > 0:
         ser.write(result)
    # #isSerialAvailable()
    ser.flush()
    time.sleep(.5)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
