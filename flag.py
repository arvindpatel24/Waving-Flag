import cv2
import os
import pyautogui

index,counter=0,True
img = cv2.imread('indiaflag.jpg')
cv2.imshow('flag',img)

os.startfile('C:/Users/Ravi/Desktop/2020 Projects/Project5_FlagWave/Vande _Mataram.mp4')


def animation():
	global index,counter,img
	if(counter):
		index = index +1
	else:
		index = index -1
	img = cv2.imread('flag_wave/'+str(index)+'.jpg')
	print(index)
	if index == 50 :
		counter = False
	elif index == 1 :
		counter = True

def play():
	animation()
	pyautogui.hotkey('ctrl','shift','x')

def pause():
	pyautogui.hotkey('ctrl','shift','z')


cam = cv2.VideoCapture(0)
_, old = cam.read()
_, new = cam.read()

Status = 0 

while(True):
	Status = Status + 1
	diff = cv2.absdiff(old, new)
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations=3)
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for contour in contours:
		(x, y, w, h) = cv2.boundingRect(contour)
		if cv2.contourArea(contour) < 3000:
			continue
		cv2.rectangle(old, (x, y), (x+w, y+h), (0, 255, 0), 2)
		#cv2.drawContours(old,contours,-1,(0,255,0),2)
		Status = 0
	if(Status<4):
		cv2.putText(old, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0), 3)
		play()
	else:
		cv2.putText(old, "Status: {}".format('Stop'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)
		pause()


	cv2.imshow("feed", old)
	cv2.imshow('flag',img)
	old = new
	_, new = cam.read()
	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows() 