import cv2 as cv
import numpy as np

img = cv.imread("./img.jpg")

height, width = img.shape[:2]
quarterHeight, quarterWidth = height/4, width/4
translationMatrix = np.float32([[1, 0, quarterWidth], [0, 1, quarterHeight]])

imgTranslated = cv.warpAffine(img, translationMatrix, (width, height))

cv.imshow("Translated", imgTranslated)
cv.waitKey(0)
cv.destroyAllWindows()