#https://www.geeksforgeeks.org/python-opencv-waitkey-function/
import cv2  

#video=cv.VideoCapture()

#https://www.youtube.com/watch?v=oXlwWbU8l2o&t=627s

my_image=cv2.imread('/Users/bobwang/Downloads/33715.png')

cv2.imshow('Robot',my_image)

cv2.waitKey(100000000)
