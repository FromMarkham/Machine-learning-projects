
import cv2  

#video=cv.VideoCapture()

#https://www.youtube.com/watch?v=oXlwWbU8l2o&t=627s

my_image=cv2.imread('/Users/bobwang/Downloads/33715.png')

#my_video=cv2.VideoCapture(1)

#cv2.imshow('Robot',my_image)

#cv2.waitKey(100000000)
#https://youtu.be/oXlwWbU8l2o?t=587
y_video=cv2.VideoCapture('//Users/bobwang/Downloads/40%20Minute%20Timer.mp4')

while True:
    isTrue,frame=y_video.read()
