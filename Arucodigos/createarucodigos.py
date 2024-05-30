import cv2
import numpy as np


makerImage = np.zeros((200,200,3),dtype=np.uint8)

getdict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

primer = cv2.aruco.generateImageMarker(getdict,1,200,makerImage,1)
segundo = cv2.aruco.generateImageMarker(getdict,50,200,makerImage,1)
tercero = cv2.aruco.generateImageMarker(getdict,24,200,makerImage,1)

cv2.imwrite("maker1.png",primer)
cv2.imwrite("maker2.png",segundo)
cv2.imwrite("maker3.png",tercero)


#%%