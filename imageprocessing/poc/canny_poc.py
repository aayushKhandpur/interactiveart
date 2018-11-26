import cv2
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
while(1):
    ret, img = cap.read()
    cv2.imshow("orig", img)
    img  =  cv2.resize(img, (80,60))
    edges = cv2.Canny(img, 100, 200)
    print edges
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    edges = cv2.Canny(img, 100, 200)
    print edges
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()



