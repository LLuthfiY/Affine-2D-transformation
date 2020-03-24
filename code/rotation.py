import cv2 
import numpy as np 


image = cv2.imread("test.jpg",1) 

def rotation(img, angle):
    img = image.copy()
    img = np.array(img)
    row, col, h = img.shape
    angle = np.deg2rad(angle)
    
    zeros = np.zeros(shape=img.shape)
    for r in range(row):
        for c in range(col):
            antiClockWise = np.array([[np.cos(angle), np.sin(angle)],[-np.sin(angle), np.cos(angle)]])
            newPosRow, newPosCol = [r, c] @ antiClockWise 
            newPosRow, newPosCol = int(newPosRow), int(newPosCol)
            if (-1< newPosCol < col) and (-1 < newPosRow < row):
                zeros[r][c] = img[newPosRow][ newPosCol]
            
    return zeros

run = rotation(image, 45)
cv2.imwrite('rotated.jpg', run)
print ('done')