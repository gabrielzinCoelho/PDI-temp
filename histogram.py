import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("./img.jpg")
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

color = ('b', 'g', 'r')

for i, c in enumerate(color):
    hist2 = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist2, color = c)
    plt.xlim([0, 256])


plt.show()
