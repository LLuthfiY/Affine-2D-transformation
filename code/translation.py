import cv2 
import numpy as np 


image = cv2.imread("test.jpg",1) 

def translation(img, arow, acol):
    img = image.copy()
    img = np.array(img)
    row, col, h = img.shape
    
    zeros = np.zeros(shape=img.shape)
    for r in range(row):
        for c in range(col):
            newPosRow = r - arow
            newPosCol = c -  acol
            if (-1< newPosCol < col) and (-1 < newPosRow < row):
                zeros[r][c] = img[r - arow][ c - acol]
            #print (img[int(r * 100/arow)][ int(c * 100/acol)])
    return zeros

run = translation(image, -10,75)
cv2.imwrite('translated.jpg', run)
print ('done')