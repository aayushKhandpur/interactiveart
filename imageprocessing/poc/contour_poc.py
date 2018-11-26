# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

imageA = cv2.imread('img1.jpg')
imageB = cv2.imread('img3.jpg')
imageA =  cv2.resize(imageA, (1000, 600))
imageB =  cv2.resize(imageB, (1000, 600))
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True, multichannel=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    #cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
#cv2.imshow("Original", imageA)
#cv2.imshow("Modified", imageB)
#cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

while 1:
    #print M
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break