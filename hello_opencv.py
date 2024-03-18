import cv2 as cv
import numpy as np

img = cv.imread("./img.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window

print(cv.__version__)
print(img.shape)

cv.destroyAllWindows()

cv.imwrite("output.jpg", img)