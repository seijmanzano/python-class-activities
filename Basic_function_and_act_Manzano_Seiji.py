import cv2 as cv

image = cv.imread('kofi.jpg')


def rescaleFrame(frame, scale=15):
    width = int(frame.shape[1] * scale / 100)
    height = int(frame.shape[0] * scale / 100)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resizedImage = rescaleFrame(image)

gray = cv.cvtColor(resizedImage, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

blur = cv.GaussianBlur(resizedImage, (3, 3), cv.BORDER_DEFAULT)

eroded = cv.erode(blur, (7, 7), iterations=5)

dilated = cv.dilate(eroded, (7, 7), iterations=5)

canny = cv.Canny(dilated, 40, 70, eroded)
cv.imshow('Canny edge', canny)

cv.waitKey(0)
