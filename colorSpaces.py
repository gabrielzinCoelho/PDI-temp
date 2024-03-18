import cv2 as cv
import numpy as np

# HSV: util para filtragem de cores (segmetação por cor)

img = cv.imread("img.jpg")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

B, G, R = img[280, 200]
T = grayImg[280, 200]

print(B, G, R)
print(T)

cv.imshow("Original", img)
cv.imshow("HSV", hsvImg)
cv.imshow("Hue channel", hsvImg[:, :, 0])
cv.imshow("Saturation channel", hsvImg[:, :, 1])
cv.imshow("Value channel", hsvImg[:, :, 2])

cv.waitKey(0)
cv.destroyAllWindows()


cv.imshow("Red channel", img[:, :, 2])
cv.imshow("Green channel", img[:, :, 1])
cv.imshow("Blue channel", img[:, :, 0])

blueChannel, greenChannel, redChannel = cv.split(img)
cv.imshow("Blue amplified", cv.merge([blueChannel+100, greenChannel, redChannel]))

cv.waitKey(0)
cv.destroyAllWindows()

zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv.imshow("Only red", cv.merge([zeros, zeros, redChannel]))
cv.imshow("Only green", cv.merge([zeros, greenChannel, zeros]))
cv.imshow("Only blue", cv.merge([blueChannel, zeros, zeros]))

cv.waitKey(0)
cv.destroyAllWindows()