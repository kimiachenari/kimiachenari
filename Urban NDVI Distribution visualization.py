"""
(G-mail: kimia.chenaari@gmail.com)
"""

"""
Image Processing Visualization Using Open-cv library. for more information visit https://github.com/opencv/opencv.
"""
#import necessary Python Libraries
import cv2 as cv
from matplotlib import pyplot as plt

#Reading image
img1 = cv.imread('.tif',0)

#Visualizing
plt.hist(img1.ravel(), bins=256, range=(5, 250), fc='k', ec='k')
plt.vlines(x=135, ymin=0, ymax=70000, colors='r')
plt.title("Mashhad, Iran") 
plt.show()


