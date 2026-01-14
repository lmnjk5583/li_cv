import cv2 as cv

cv.imread("/mnt/c/ex/ML/img/logo.jpg")

logo_per=cv.imread("/mnt/c/ex/ML/img/logo.jpg")

cv.imshow('logo_per', logo_per)
cv.waitKey()
cv.destroyAllWindows() 