import cv2 as cv
import numpy as np

def showImage(title, img):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def cleanImg():
    return np.zeros((512, 512, 3), dtype = "uint8")


img = cleanImg()
showImage("Screen", img)

cv.line(img, (0, 0), (511, 511), (0, 0 , 255), 5)
showImage("Screen with line", img)

img = cleanImg()
cv.rectangle(img, (100, 100), (411, 200), (0, 255, 0), -1)
showImage("Screen with rectangle", img)

img = cleanImg()
cv.circle(img, (256, 256), 100, (255, 0, 0), -1)
showImage("Screen with circle", img)

img = cleanImg()
pts = np.array([[110, 50], [500, 50], [190, 200], [150, 500]], dtype="int32")
pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (100, 200, 80), 5)
showImage("Boomerang", img)

img = cleanImg()
cv.putText(img, "Hello World", (50, 200), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2.5, (100, 70, 200), 5)
showImage("Text", img)