import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(20,20),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"mecury",(50,50),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,255))
cv2.putText(img,"venus",(180,80),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=1,color=(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(10000)