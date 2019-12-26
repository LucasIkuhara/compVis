import cv2
import numpy as np
import time as t

cap = cv2.VideoCapture(0)
FPS = 0
lastSec = t.time()

#Filter kernel examples
#https://en.wikipedia.org/wiki/Kernel_(image_processing)

#Gauss
Kernel1 = np.array([(1, 2, 1),
                    (2, 4, 2), 
                    (1, 2, 1)])/16

#Sobel
Kernel2 = np.array([(-1, -1, -1),
                    (-1,  8, -1), 
                    (-1, -1, -1)])

LT, UT = int(input("Lower Threshold:")), int(input("Upper Threshold:"))

while(True):
    if t.time() > lastSec+1:
        lastSec = t.time()
        print("FPS: ",FPS)
        FPS=0
    
    #ret is a boolean which acts a flag regarding whether read() was successful
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Input Video", frame)
    cv2.imshow("Grayscale Video", gray)
    
    filtered = cv2.filter2D(gray, -1, Kernel1)
    cv2.imshow("Gaussian Blur Video", filtered)
    filtered = cv2.filter2D(gray, -1, Kernel2)
    cv2.imshow("Gauss B. + Sobel Video", filtered)

    filtered = cv2.Canny(filtered, LT, UT)
    cv2.imshow("Canny", filtered)

    FPS += 1

    #makes it so you can close the program by pressing ESC.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()