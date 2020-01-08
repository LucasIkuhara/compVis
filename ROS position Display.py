import numpy as np
import random as r
import sys
import rospy as ros
from nav_msgs.msg import Odometry

#Famosa Gamb
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 as cv
#ROS openCV no python 3

def mapSetup(img, interval):
    darkGreen = np.array([0, 60, 0], np.uint8)
    lightGreen = np.array([0, 150, 0], np.uint8)
    darkRed = np.array([0, 0, 60], np.uint8)
    lightRed = np.array([0, 0, 150], np.uint8)

    Xinterval = np.size(img, 0) // interval
    Yinterval = np.size(img, 1) // interval

    for i in range(0, Yinterval):
        for j in range(0, np.size(map,1)):
            if i*interval == np.size(img, 1)//2:
                img[i*interval][j] = lightGreen
            else:
                img[i*interval][j] = darkGreen

    for i in range(0, Xinterval):
        for j in range(0, np.size(map,0)):
            if i*interval == np.size(img, 0)//2:
                img[j][i*interval] = lightRed
            else:
                img[j][i*interval] = darkRed
    
    return map


class Robot():
    def __init__(self, stX, stY, stZ):
        self.startingPos = [stX, stY, stZ]
        self.pos = [stX, stY, stZ]
        posSub = ros.Subscriber("/my_odometry/filtered", Odometry, self.odomCallback)

    def odomCallback(self, data):
        self.pos = [int(self.startingPos[0] + data.x),
        int((self.startingPos[1] + data.y)*10), int((self.startingPos[2] + data.y)*10)]

    def drawRobot(self, map):
        try:
            shape = [(0,0), (0, 2), (0, -2), (1, 2), (1, -2), (2, 2), (2, -2), (-1, 2), (-1, -2),
                     (-2, 2), (-2, -2), (-3, -1), (-3, 0), (-3, 1), (3, -1), (3, 0), (3, 1),
                     (3, -3), (3, 3), (-3, 3), (-3, -3) ]
            for i in range(len(shape)):
                map[self.pos[0] + shape[i][0], self.pos[1] + shape[i][1]] = np.array([250, 150, 150], np.uint8)

        except:
            pass
        return map


mapSize = (180, 180)
bot = Robot(mapSize[0]//2, mapSize[1]//2, 0)

while True:
    map = np.zeros((mapSize[0], mapSize[0], 3), np.uint8)
    map = mapSetup(map, 10)
    map = bot.drawRobot(map)    
    
    map = cv.resize(map, (700, 700), interpolation = cv.INTER_AREA )
    cv.imshow('Map', map)
    cv.waitKey(200)
    #cv.destroyAllWindows()