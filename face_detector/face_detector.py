import cv2
#if you want to use random colors for the boxes use the following code
#from random import randrange

#load some pretrained data from harcascade
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect the faces in
#img = cv2.imread('1.jpg')

#to capture video from webcam
webcam=cv2.VideoCapture(0) #0 is the default webcam or a video file

#must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect the faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangles around the faces
#the last 2 is the thickness, 10 is the thickest. The second tuple is the
#size of the sqaure so we can add it to the coordnates of the upper left hand coordinate
#cv2.rectangle(img, (48,92), (48+232,92+232), (0,255,0), 2)

for (x,y,w,h) in face_coordinates:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
#print(face_coordinates)

#display the images with the faces
cv2.imshow('Basic face detector', img)
cv2.waitKey()



print('Code completed')
