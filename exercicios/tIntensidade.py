import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("pollen.jpg", 0) 
height, width = img.shape[:2]
imgFinal = np.zeros((height, width), dtype="uint8")
funcao = np.zeros(256, dtype="uint8")

r1 = 97
s1 = 30
r2 = 126
s2 = 150
a1 = s1/r1
a2 = (s2 - s1)/(r2 - r1)
a3 = (255 - s2)/(255 - r2)

for i in range(256):
    if (i < r1):
        funcao[i] = int(a1 * i)
    elif (i <= r2):
        funcao[i] = int(s1 + a2 * (i - r1))
    else:
        funcao[i] = int(s2 + a3 * (i - r2))

for i in range(height):
    for j in range(width):
        imgFinal[i, j] = funcao[img[i, j]]

cv.imshow("Original", img)
cv.imshow("Transformacao de Intensidade", imgFinal)
cv.waitKey(0)
cv.destroyAllWindows()

hist = cv.calcHist([img], [0], None, [256], [0, 256])
histFinal = cv.calcHist([imgFinal], [0], None, [256], [0, 256])

plt.hist(img.ravel(), 256, [0, 256])
# plt.plot(hist, color='b')
plt.hist(imgFinal.ravel(), 256, [0, 256])

plt.show()