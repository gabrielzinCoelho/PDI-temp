import cv2 as cv
import numpy as np

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

img = cv.imread("img.jpg")

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        img[i, j] = abs(255 - img[i, j])

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()

width, height = img.shape[:2]
centerX, centerY = width//2, height//2
img = np.concatenate(
    (
        np.concatenate((
            img[centerX:width, centerY:height, :],
            img[0:centerX, centerY:height, :]
        )),
        np.concatenate((
            img[centerX:width, 0:centerY, :],
            img[0:centerX, 0:centerY, :]
        ))
    ), 
    axis = 1
)

cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()
