import cv2
import numpy as np
import time as t
import random as rnd
import math


def randomWalkSampler(picture, n=30):
    samples = []
    dim = picture.shape
    for i in range(n):
        pixel = picture[rnd.randint(0, dim[0]-1)][rnd.randint(0, dim[1]-1)]
        samples.append(pixel)
    sum = 0
    for elem in samples:
        for value in elem:
            sum += value
    return sum/(len(samples)*3)

def colorBoundariesGenerator(color, threshold=15):
    aux = np.array((threshold, threshold, threshold))
    bright = color + aux
    dark = color - aux

    for i in range(3):
        if dark[i]>255:
            dark[i] = 255
        if dark[i]<0:
            dark[i] = 0

    for i in range(3):
        if bright[i]>255:
            bright[i] = 255
        if bright[i]<0:
            bright[i] = 0

    return dark, bright

def colorScalling(color, originalBright, actualBright):
    pass

def colorSelect(cap):
    dim = cap.read()[1].shape
    centerPoint = (int(dim[0]/2), int(dim[0]/2))
    point1 = (centerPoint[0]-20, centerPoint[1]-20)
    point2 = (centerPoint[0]-20, centerPoint[1]+20)
    point3 = (centerPoint[0]+20, centerPoint[1]+20)
    point4 = (centerPoint[0]+20, centerPoint[1]-20)
    red = (0, 0, 255)

    while(True):
        ret, frame = cap.read()
        #Draw Square
        cv2.line(frame, point1, point2, red )
        cv2.line(frame, point2, point3, red )
        cv2.line(frame, point3, point4, red )
        cv2.line(frame, point4, point1, red )
        cv2.imshow("Choose a color by pressing space", frame)
        
        #Choose a color by pressing space.
        k = cv2.waitKey(30) & 0xff
        if k == 32:
            break
    
    cv2.destroyAllWindows()

    #Store All pixels within the red border
    pixels = []
    for i in range(point1[0], point3[0]):
        for j in range(point1[1], point3[1]):
            pixels.append(frame[i][j])

    #Get and return the mean of each color value
    B_sum = G_sum = R_sum = 0
    for i in range(len(pixels)):
        B_sum += pixels[i][0]
        G_sum += pixels[i][1]
        R_sum += pixels[i][2]
    mean = lambda val: int(val/len(pixels))

    return np.array([mean(B_sum), mean(G_sum), mean(R_sum)]) 


cap = cv2.VideoCapture(0)
#TargetColor = (int(input("R: ")), int(input("G: ")), int(input("B: ")))
walkDistance = int(input("Brightness Samples: "))
threshold = int(input("Color Threshold: "))
TargetColor = colorSelect(cap)
print("Selected color: ", TargetColor)
FPS = 0
lastSec = t.time()


while(True):
    #ret is a boolean which acts a flag regarding whether read() was successful
    ret, frame = cap.read()
    targetDark, targetBright = colorBoundariesGenerator(TargetColor, threshold)
    mask = cv2.inRange(frame, targetDark, targetBright)
    cv2.imshow("Input Video", frame)
    cv2.imshow("Segmented Video", mask)
    meanBrightness = randomWalkSampler(frame, 100)
    
    FPS += 1
    if t.time() > lastSec+1:
        lastSec = t.time()
        print("FPS: ",FPS)
        FPS=0

    #makes it so you can close the program by pressing ESC.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()