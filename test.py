import cv2
import matplotlib.pyplot as plt
import math
import numpy as np

img = cv2.imread('indiaflag.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
rows,cols=img.shape[:2]
img_output = np.zeros((rows,cols,3),dtype='uint8')
t,index=-50,0

while(True):
	index = index +1
	for i in range(rows):
	    for j in range(cols):
	        offset_y = int(10.0*math.sin(2*3.14*j/ 180))
	        offset_x = 0 + t
	        if ((i+offset_y) < rows) and (j+offset_x < cols) and (j+offset_x > 0):
	            for k in range(3):
	                img_output[i][j][k] = img[(i+offset_y)][(j+offset_x)][k]
	        else:
	            for k in range(3):
	                img_output[i][j][k] = 0
	t=t+2
	if(t>50):
		t=1
	#cv2.imwrite('flag_wave/'+str(index)+'.jpg',img_output)
	cv2.imshow('flag_wave',img_output)
	if(cv2.waitKey(1)==ord('q')):
		break