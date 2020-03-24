## sistem pakar 112 Asssignment 1 Task 1
# Affine-2D-transformation

Muhammad Luthfi A
1313617033

transformation image berupa array 2D dengan python

scaling, translate, dan rotation dilakukan dengan mengkalikan setiap coordinatnya dengan [affine transformation matrix](https://en.wikipedia.org/wiki/Affine_transformation)
# Scaling

menggunakan Matrix
```
[[scaleX,     0, 0],
 [     0,scaleY, 0],
 [     0,     0, 1]]
```
 # Translating
 
 menggunakan Matrix
 ```
[[1, 0, TranslateX],
 [0, 1, TranslateY],
 [0, 0,          1]]
```
# Rotation 

menggunakan Matrix
```
[[cos(theta), -sin(theta), 0],
 [sin(theta),  cos(theta), 0],
 [         0,           0, 1]]
```
# projectives 

![Azunyan wanna be a kaichoo of keiOnBu](https://github.com/LLuthfiY/Affine-2D-transformation/blob/master/img/projTransformed_FIXLAH.jpg)
berdasarkan [artikel](https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog) ini
projective transformation dilakukan dengan mengkalikan setiap coordinate dengan matrix 
```
[[ H00, H01, H02],
 [ H10, H11, H12],
 [ H20, H21, H22]]
```
yang dimana kita dikasih kebebasan untuk mengisi setiap element matrix, untuk melakukan hal tersebut kita membutuhkan 4 coordinate awal dan 4 coordinate akhir, lalu satu coordinate awal akan di bandingkan dengan satu coordinate akhir.

## How they are Translated to code

dengan mengkalikan setiap pixel dengan matrix yang didapat
```
def 
...
for r in range(row):
        for c in range(col):
            newrow, newcol = matrix @ [r, c]
            newrow, newcol = int(newrow), int(newcol)
            zeros[newrow][newcol] = img[r][c]
...
```
## interesting things i found while experimenting the program

![sad](https://github.com/LLuthfiY/Affine-2D-transformation/blob/master/img/scalledOri.jpg)

terdapat rongga saat men scaling jika menggunakan affine matrix 

hal itu karena affine hanya merubah posisi

```
[A][B] --> [A][ ][B][ ]
[C][D]     [ ][ ][ ][ ]
           [C][ ][D][ ]
           [ ][ ][ ][ ]
```

maka dari itu saya merubah code nya yang awalnya 

```
for r in range(row):
        for c in range(col):
            newrow, newcol = [r,c] @ np.array([[arow,0],
                                               [0,acol]])
            newrow, newcol = int(newrow), int(newcol)
            zeros[newrow][newcol] = img[r][c]
```
menjadi
```
for r in range(zeros.shape[0]):
        for c in range(zeros.shape[1]):
            newrow, newcol =  np.array([[1/arow ,0],
                                        [0, 1/acol]]) @ np.array([r, c]).T
            newrow, newcol = int(newrow), int(newcol)
            zeros[r][c] = img[newrow][newcol]
```
```
[A][B] --> [A][A][B][B]
[C][D]     [A][A][B][B]
           [C][C][D][D]
           [C][C][D][D]
```
