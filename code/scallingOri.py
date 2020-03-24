import cv2 
import numpy as np 


image = cv2.imread("test2.jpg",1) 


def scalling (image, arow=1, acol=1): #acol and arow in percent
    img = image.copy()
    img = np.array(img)
    row, col, h = img.shape
    maxx = max(row,col,h)

    
    zeros = np.zeros(shape=(int(row*arow), int(col*acol), 3))
    for r in range(row):
        for c in range(col):
            newrow, newcol = [r,c] @ np.array([[arow,0],[0,acol]])
            newrow, newcol = int(newrow), int(newcol)
            zeros[newrow][newcol] = img[r][c]
            #print (img[int(r * 100/arow)][ int(c * 100/acol)])
             
    return zeros
        
    

run = scalling(image, 2,2)
cv2.imwrite('scalledOri.jpg', run)
print ('done')