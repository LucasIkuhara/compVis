import cv2 
import numpy as np
import rospy
from robosub_msgs.msg import Euler
from math import sin, cos

output_dimensions = [480, 720]
rospy.init_node("cnn_prokector")
orientation = np.array((0,0,0), dtype=np.float)
directionVector = np.array((0,0,0), dtype=np.float)

def orientationCallback(data):
    orientation[0] = eulerNormalization(data.roll)
    orientation[1] = eulerNormalization(data.pitch)
    orientation[2] = eulerNormalization(data.yaw)
    print("roll: {}, pitch: {}, yaw: {}".format(orientation[0], orientation[1], orientation[2]))

    directionVector[0] = cos(orientation[2])*cos(orientation[1])
    directionVector[1] = sin(orientation[2])*cos(orientation[1])
    directionVector[2] = sin(orientation[1])
    print("Directional Vector: ", directionVector)

def eulerNormalization(ang):
    if ang <= 180:
        return ang
    else:
        return abs(360-ang)

rospy.Subscriber("pretty/orientation", Euler, orientationCallback)

while True:
    image = np.zeros(output_dimensions, dtype=np.uint8)
    cv2.imshow("draw", image)

    if  0xFF & cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
rospy.spin()