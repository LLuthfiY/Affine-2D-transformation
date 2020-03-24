import cv2 
import numpy as np 
azunyan = cv2.imread("azunyan3.jpg",1) 
billboard = cv2.imread("bb2.jpg",1)
def find4variable(image, bg, p) :
    row, col, h = image.shape
    bgr, bgc, h = bg.shape
    pointImage = [[0, 0],[0, col],[row, 0],[row, col]]
    H = []
    for i in range(0, len(p)):
        x, y = pointImage[i][0], pointImage[i][1]
        u, v = p[i][0], p[i][1]
        H.append([x, y, 1, 0, 0, 0, -u*x, -u*y, -u])
        H.append([0, 0, 0, x, y, 1, -v*x, -v*y, -v])
    H = np.asarray(H)
    U, S, Vh = np.linalg.svd(H)
    L = Vh[-1,:] / Vh[-1,-1]
    H = L.reshape(3, 3)
    
    return H
    
def projtrans(image, bg, p):
    row, col, h = image.shape
        
    H = find4variable(image, bg, p)
    
    

    for r in range(row):
        for c in range(col):
            newRow, newCol, scale = H @ np.array([r, c, 1])
            newRow, newCol = int(newRow/scale), int(newCol/scale) 
            bg[newRow, newCol] = image[r, c]
            
            
    return bg



run = projtrans(azunyan, billboard ,((221, 258), (281, 524),(354, 241), (395, 537)))
cv2.imwrite('projTransformed_FIXLAH.jpg', run)
print ('done')  
