import pytesseract
import numpy as np
import cv2
from scipy.misc import imread, imresize,imshow
import skimage.transform
image = cv2.imread('img2.jpg')
cv2.imshow('orignal',image)   


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)       
cv2.imwrite('gray.jpg', gray)

ret2,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('threshold',thresh)                

cv2.imwrite('thresh.jpg', thresh)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('blur',blurred) 
cv2.imwrite('blur.jpg', blurred)



text = pytesseract.image_to_string(blurred)
print(text)
cv2.waitKey(0)
