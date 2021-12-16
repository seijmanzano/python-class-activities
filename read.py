import cv2 as cv

img = cv.imread('img-outside.jpg')

# function to resize img
def rescaleFrame(frame, scale = 15):
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resizedImage = rescaleFrame(img)

# converting to grayscale
gray = cv.cvtColor(resizedImage, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# blur
blur = cv.GaussianBlur(resizedImage, (3,3), cv.BORDER_DEFAULT)

# eroded
eroded = cv.erode(blur, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# dilating the img
dilated = cv.dilate(eroded, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# edge cascade
canny = cv.Canny(dilated, 70, 100)
cv.imshow('Canny', canny)

cv.waitKey(0)