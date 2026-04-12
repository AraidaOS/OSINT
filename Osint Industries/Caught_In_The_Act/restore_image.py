"""
Open image, try and restore original, clean image by removing doodle as much as possible usint OpenCV

::@author:: T.A.
"""

import cv2
import numpy as np

image = cv2.imread("<Image_File>")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv.inRange(hsv, lower_red1, upper_red1)
mask2 = cv.inRange(hsv. lower_red2, upper_red2)

mask = mask1 + mask2

result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
cv2.imwrite("restored_img.jpg")
