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
    
    """#get ratio for scalling image------------------------------------------------------
    RightUpRow, RightUpCol, scale = H @ np.array([0, col -1, 1]).T
    RightUpRow, RightUpCol = int(RightUpRow/scale), int(RightUpCol/scale) 
    
    leftBottomRow, leftBottomCol, scale = H @ np.array([row -1, 0, 1]).T
    leftBottomRow, leftBottomCol = int(leftBottomRow/scale), int(leftBottomCol/scale) 
    
    firstpixelRow, firstpixelCol, scale = H @ np.array([0, 0, 1]).T
    firstpixelRow, firstpixelCol = int(firstpixelRow/scale), int(firstpixelCol/scale)
    
    ratioR = np.sqrt((p[2][0] - p[0][0])**2 + (p[2][1] - p[0][1])**2 ) / np.sqrt((leftBottomRow - firstpixelRow)**2 + (leftBottomCol - firstpixelCol)**2)
    ratioC = np.sqrt((p[1][0] - p[0][0])**2 + (p[1][1] - p[0][1])**2 ) / np.sqrt((RightUpRow - firstpixelRow)**2 + (RightUpCol - firstpixelCol)**2)
    
    print (ratioR)
    print (np.sqrt((p[1][0] - p[0][0])**2 + (p[1][1] - p[0][1])**2 ), '  /  ', np.sqrt((RightUpRow - firstpixelRow)**2 + (RightUpCol - firstpixelCol)))
    print (image.shape)
    print ('bg', billboard.shape)
    image = scalling(image, ratioR, ratioC)
    print (image.shape)
    row, col, h = image.shape
    
    
    #---------------------------------------------------------------------------------
    
""" 
    for r in range(row):
        for c in range(col):
            newRow, newCol, scale = H @ np.array([r, c, 1])
            newRow, newCol = int(newRow/scale), int(newCol/scale) 
            bg[newRow, newCol] = image[r, c]
            
            
    return bg

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


run = projtrans(azunyan, billboard ,((221, 258), (281, 524),(354, 241), (395, 537)))
cv2.imwrite('projTransformed_FIXLAH.jpg', run)
print ('done')  