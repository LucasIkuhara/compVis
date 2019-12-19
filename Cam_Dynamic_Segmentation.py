import cv2
import numpy as np
import time as t
import random as rnd


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

def colorNormalizer(color):
    for i in range(3):
        if color[i]>255:
            color[i] = 255
        if color[i]<0:
            color[i] = 0
    return color

def colorBoundariesGenerator(color, threshold=15):
    aux = np.array((threshold, threshold, threshold))
    bright = color + aux
    dark = color - aux
    
    bright = colorNormalizer(bright)
    dark = colorNormalizer(dark)

    return dark, bright

def colorScallingAdditive(color, originalBright, currentBright):
    delta = currentBright - originalBright 
    color = color + np.array([delta, delta, delta])
    color = colorNormalizer(color)
    
    return color

def colorScallingPercentual(color, originalBright, currentBright):
    k = originalBright/currentBright
    color = np.array([color[0]*k, color[1]*k, color[2]*k])
    color = colorNormalizer(color)

    return color

def colorSelect(cap, brightnessSamples=30):
    dim = cap.read()[1].shape
    centerPoint = (int(dim[1]/2), int(dim[0]/2))
    
    point1 = (centerPoint[0]-20, centerPoint[1]-20)
    point2 = (centerPoint[0]-20, centerPoint[1]+20)
    point3 = (centerPoint[0]+20, centerPoint[1]+20)
    point4 = (centerPoint[0]+20, centerPoint[1]-20)
    red = (0, 0, 255)

    while(True):
        ret, frame = cap.read()
        #Draw Square
        cv2.line(frame, point1, point2, red, 2 )
        cv2.line(frame, point2, point3, red, 2 ) 
        cv2.line(frame, point3, point4, red, 2 )
        cv2.line(frame, point4, point1, red, 2 )
        
        cv2.imshow("Choose a color by pressing space", frame)
        
        #Choose a color by pressing space.
        k = cv2.waitKey(30) & 0xff
        if k == 32:
            break
    
    cv2.destroyAllWindows()

    #Store All pixels within the red border
    pixels = []
    for i in range(point1[1], point3[1]):
        for j in range(point1[0], point3[0]):
            pixels.append(frame[i][j])

    #Get and return the mean of each color value
    B_sum = G_sum = R_sum = 0
    for i in range(len(pixels)):
        B_sum += pixels[i][0]
        G_sum += pixels[i][1]
        R_sum += pixels[i][2]
    mean = lambda val: int(val/len(pixels))

    color = np.array([mean(B_sum), mean(G_sum), mean(R_sum)])
    
    #Show the chosen color
    display = np.zeros((1, 1, 3), np.uint8)
    display[0][0] = color
    display = cv2.resize(display, (100, 100))
    cv2.imshow("Chosen color:", display)

    return color, randomWalkSampler(frame, brightnessSamples) 


cap = cv2.VideoCapture(0)
walkDistance = int(input("Brightness Samples: "))
threshold = int(input("Color Threshold: "))
TargetColor, TargetColorBrightness = colorSelect(cap)
print("Selected color: ", TargetColor)
FPS = 0
lastSec = t.time()


while(True):
    #ret is a boolean which acts a flag regarding whether read() was successful
    ret, frame = cap.read()
    meanBrightness = randomWalkSampler(frame, walkDistance)
    cv2.imshow("Input Video", frame)

    #regular segmentation
    targetDark, targetBright = colorBoundariesGenerator(TargetColor, threshold)
    mask = cv2.inRange(frame, targetDark, targetBright)
    cv2.imshow("Normal segmentation", mask)

    #Gauss filter
    frame = cv2.filter2D(frame, -1, (np.array([(1, 2, 1), (2, 4, 2), (1, 2, 1)])/16) )

    #addition-based correction
    colorScallingAdditive(TargetColor, TargetColorBrightness, meanBrightness)
    targetDark, targetBright = colorBoundariesGenerator(TargetColor, threshold)
    mask = cv2.inRange(frame, targetDark, targetBright)
    cv2.imshow("Segmented with additive correction", mask)
    
    #percentage-based correction
    colorScallingPercentual(TargetColor, TargetColorBrightness, meanBrightness)
    targetDark, targetBright = colorBoundariesGenerator(TargetColor, threshold)
    mask = cv2.inRange(frame, targetDark, targetBright)
    cv2.imshow("Segmented with percentual correction", mask)

    FPS += 1
    if t.time() > lastSec+1:
        lastSec = t.time()
        print("FPS: ",FPS)
        print("Mean Brightness: ",meanBrightness)
        FPS=0

    #makes it so you can close the program by pressing ESC.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()