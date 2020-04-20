import cv2 
import numpy as np

output_dimensions = [480, 720]


while True:
    image = np.zeros(output_dimensions, dtype=np.uint8)
    cv2.imshow("draw", image)

    if  0xFF & cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()