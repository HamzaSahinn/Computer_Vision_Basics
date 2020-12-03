# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:25:06 2020

@author: Abdullah Hamza Şahin
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

#İstanbul Arkeoloji Museum
original_image = cv2.imread("./input/Museum.png")
dims = original_image.shape

#Section a

crop_height = int(dims[0]/4)
crop_width = int(dims[1]/4)

half_image = original_image[crop_height:dims[0]-crop_height, crop_width: dims[1]-crop_width, ::]
half_dims = half_image.shape

cv2.imwrite("./output/half_Museum.png" , half_image)
cv2.imshow("half_Museum", half_image)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()

##############################################################
#Section b

#Channel order is BGR
red_channel = original_image[::,::,2]
blue_channel = original_image[::, ::, 0]

changed_image = original_image.copy()

changed_image[::,::,0] = red_channel
changed_image[::, ::, 2] = blue_channel
cv2.imwrite("./output/channel_changed_Museum.png", changed_image)
cv2.imshow("channel_changed_Museum", changed_image)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()
##############################################################

#section c

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./output/grayscale_Museum.png", gray_image)
cv2.imshow("gray_Museum", gray_image)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()

##############################################################

#Section d

im = cv2.imread("./input/Museum.png").astype(np.float32)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
 
#For better detection blurring
gray = cv2.GaussianBlur(im, (5,5), 1)
gray /=255.0

kernelx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype = np.float32)
kernely = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype = np.float32)


gradient_x = cv2.filter2D(gray, -1, kernelx)
gradient_y = cv2.filter2D(gray, -1, kernely)

#Calculate the gradient magnitude
gradient_magnitude = np.hypot(gradient_x, gradient_y)

dx = gradient_x*255.0
dy = gradient_y*255.0

cv2.imwrite("./output/gradientx.png", dx)
cv2.imwrite("./output/gradienty.png", dy)

cv2.imshow("gradientx", gradient_x)
cv2.imshow("gradienty", gradient_y)

cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()



orientation = cv2.phase(dx, dy, angleInDegrees=True)

thresh = 100
_, binary_image = cv2.threshold(gradient_magnitude*255.0, thresh, 255, cv2.THRESH_BINARY)

red = np.array([0, 0, 255])
green = np.array([0, 255, 0])
cyan = np.array([255, 255, 0])
yellow = np.array([0, 255, 255])
blue = np.array([255,0,0])
pink = np.array([255,0,255])

gradient_orien_map = np.zeros((orientation.shape[0], orientation.shape[1], 3), dtype=np.uint8)


gradient_orien_map[ (binary_image == 255) & (orientation < 90) ] = red
gradient_orien_map[(binary_image == 255) & (orientation >= 90) & (orientation < 135)] = cyan
gradient_orien_map[(binary_image == 255) & (orientation >= 135) & (orientation < 180)] = blue
gradient_orien_map[(binary_image == 255) & (orientation >= 180) & (orientation < 225)] = green
gradient_orien_map[(binary_image == 255) & (orientation >= 225) & (orientation < 270)] = pink
gradient_orien_map[(binary_image == 255) & (orientation >= 270)] = yellow



# just for showing it with opencv, replace it with matplotlib if you prefer
cv2.imshow("Gradient_Orientation", gradient_orien_map)
cv2.imshow("gradient_magnitude",gradient_magnitude)

cv2.imwrite("./output/Gradient_orientation.png", gradient_orien_map)
cv2.imwrite("./output/gradient_magnitude.png", gradient_magnitude*255.0)

cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()

cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()
############################################################

#Section e
original_image = cv2.imread("./input/Museum.png")
gray_scale_museum = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)


sigma1 = ndimage.gaussian_laplace(gray_scale_museum, sigma=1)
sigma2 = ndimage.gaussian_laplace(gray_scale_museum, sigma=2)
sigma3 = ndimage.gaussian_laplace(gray_scale_museum, sigma=3)
sigma4 = ndimage.gaussian_laplace(gray_scale_museum, sigma=4)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.imshow(sigma1)
ax1.set_title("Sigma=1")
ax1.get_xaxis().set_visible(False)

ax2.imshow(sigma2)
ax2.set_title("Sigma=2")
ax2.get_xaxis().set_visible(False)

ax3.imshow(sigma3)
ax3.set_title("Sigma=3")
ax3.get_xaxis().set_visible(False)

ax4.imshow(sigma4)
ax4.set_title("Sigma=4")
ax4.get_xaxis().set_visible(False)



cv2.imshow("Sigma1_LoG", sigma1)
cv2.imshow("Sigma2_LoG", sigma2)
cv2.imshow("Sigma3_LoG", sigma3)
cv2.imshow("Sigma4_LoG", sigma4)



cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()
##########################################################



