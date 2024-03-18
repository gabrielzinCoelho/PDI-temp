import cv2 as cv
import numpy as np

img = cv.imread("img.jpg")
angle = 90

height, width = img.shape[:2]
rotationMatrix = cv.getRotationMatrix2D((width/2, height/2), angle, 1)
rotatedImg = cv.warpAffine(img, rotationMatrix, (width, height))

rotatedImg2 = cv.transpose(img)
cv.imshow("Imagem rotacionada ({} graus)".format(angle), rotatedImg2)
cv.waitKey()
cv.imshow("Imagem rotacionada ({} graus)".format(angle), rotatedImg)
cv.waitKey()
cv.destroyAllWindows()
