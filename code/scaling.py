import cv2 
import numpy as np 


image = cv2.imread("test2.jpg",1) 


def scalling (image, arow=1, acol=1): #acol and arow in percent
    img = image.copy()
    img = np.array(img)
    row, col, h = img.shape
    
    newrow, newcol = int(row*arow), int(col*acol)
    
    zeros = np.zeros(shape=(newrow, newcol, 3))
    for r in range(zeros.shape[0]):
        for c in range(zeros.shape[1]):
           
            newrow, newcol =  np.array([[1/arow ,0],
                                        [0, 1/acol]]) @ np.array([r, c]).T
            newrow, newcol = int(newrow), int(newcol)
            
            zeros[r][c] = img[newrow][newcol]
             
    return zeros
        
    

run = scalling(image, 1.75,1.75)
cv2.imwrite('scalled.jpg', run)
print ('done')