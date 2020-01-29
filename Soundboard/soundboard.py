import cv2 
import winsound as wsnd
import time
import numpy as np

# Numpad 48 to 56
soundboard = {
              49: "test.wav",
              50: "test.wav",
              51: "test.wav",
              52: "test.wav",
              53: "test.wav",
              54: "test.wav",
              55: "test.wav",
              56: "test.wav",
              57: "test.wav"}



mat = np.zeros((50, 250, 3), np.uint8)

while True:
    cv2.imshow("Soundboard", mat)
    lastkey = cv2.waitKey(30) & 0xff
    
    #ESC to quit
    if lastkey == 27:
        break
 
    if lastkey != 255:
        try:
            print(soundboard[lastkey])
            #wsnd.Beep(soundboard[lastkey], 1000)
            wsnd.PlaySound(soundboard[lastkey], wsnd.SND_FILENAME | wsnd.SND_ASYNC)
        except:
            print('No matching sound for key "{}" or missing file.'.format(lastkey))