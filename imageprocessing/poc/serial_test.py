import cv2
import serial, time
import struct

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial('COM3', 9600, timeout=.25)

if ser.isOpen():
    print(ser.name + ' is open...')

while (1):
   # ser.write('1111')
    ser.write('1234')
    print ser.readline()
    #ser.write('1234')
    time.sleep(1)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# s.read()


# time.sleep(3) # wait a couple seconds
# # buf = bytearray('ascii')
# # buf += struct.pack('>B', 0)
# # buf += struct.pack('>B', 1)
# s.write(struct.pack('>BBB',0,1,1))
# print s.readline()
# time.sleep(.5)
