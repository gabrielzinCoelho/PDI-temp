import cv2 as cv
import numpy as np

img = cv.imread("./img.jpg")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Original", img)
cv.waitKey(0)

# cv.destroyAllWindows()

cv.imshow("Gray Scale", grayImg)
cv.waitKey(0)

cv.destroyAllWindows()


grayImg_2 = cv.imread("img.jpg", 0)
cv.imshow("Gray Scale", grayImg_2)
cv.waitKey(0)
cv.destroyAllWindows()