import cv2 
import numpy as np 
azunyan = cv2.imread("azunyan2.jpg",1) 
billboard = cv2.imread("bb2.jpg",1)
def scalling (image, arow=100, acol=100): #acol and arow in percent
    img = image.copy()
    img = np.array(img)
    row, col, h = img.shape
    
    newrow, newcol = int(row*arow/100), int(col*acol/100 )
    
    zeros = np.zeros(shape=(newrow, newcol, 3))
    for r in range(newrow):
        for c in range(newcol):
           
            zeros[r][c] = img[int(r * 100/arow)][ int(c * 100/acol)]
            #print (img[int(r * 100/arow)][ int(c * 100/acol)])
             
    return zeros

def projtrans(image, bg, p) :
    row, col, h = image.shape
    bgr, bgc, h = bg.shape
    pointImage = [[0, 0],[0, bgc],[bgr, 0],[bgr, bgc]]
    A = []
    
    for i in range(0, len(p)):
        x, y = pointImage[i][0], pointImage[i][1]
        u, v = p[i][0], p[i][1]
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y, -u])
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y, -v])
    A = np.asarray(A)
    U, S, Vh = np.linalg.svd(A)
    L = Vh[-1,:] / Vh[-1,-1]
    H = L.reshape(3, 3)
    print (H)
    
    maxscale = 0
    for r in range(row):
        for c in range(col):
            newRow, newCol, scale = H @ np.array([r, c, 1]).T
            
            newRow, newCol = int(newRow/scale), int(newCol/scale) 
            
            bg[newRow, newCol] = image[r, c]
            if (scale > maxscale):
                maxscale = scale
    print (maxscale)
    return bg
azunyan = scalling(azunyan, 128, 128)
run = projtrans(azunyan, billboard ,((221, 258), (281, 524),(354, 241), (395, 537)))
cv2.imwrite('projTransformed_FIXLAH_test.jpg', run)
print ('done')  