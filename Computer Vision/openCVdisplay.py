import numpy as np
import cv2 as cv
import random as r

#img = cv.imread("8bit.png")
#cv.imshow('dg', img)suspendue
#cv.waitKey(800)

while True:
    a = np.zeros((100, 100, 3), np.uint8)
    axis = (r.randint(0, 99), r.randint(0, 99))
    try:
        a[axis[0]][axis[1]] = np.array([255, 255, 100], np.uint8)
        a[axis[0]][axis[1]+3] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+1][axis[1]+1] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+1][axis[1]+2] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+2][axis[1]+1] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+2][axis[1]+2] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+3][axis[1]] = np.array([255, 255, 100], np.uint8)
        a[axis[0]+3][axis[1]+3] = np.array([255, 255, 100], np.uint8)
    except:
        pass

    a =cv.resize(a, (700, 700), interpolation = cv.INTER_AREA )
    cv.imshow('Map', a)
    cv.waitKey(200)
    #cv.destroyAllWindows()