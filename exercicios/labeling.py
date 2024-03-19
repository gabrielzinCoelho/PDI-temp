import cv2 as cv
import numpy as np

img = cv.imread("bolhas.png", 0)
height, width = img.shape[:2]

counter = 0

for i in range(height):
    for j in range(width):
        if(img[i, j] == 255):
            counter+= 1
            cv.floodFill(img, None, (j, i), counter)

print("{} bolhas".format(counter))
cv.imshow("Image", img)
cv.waitKey()
cv.destroyAllWindows()