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

projective transformation dilakukan dengan mengkalikan setiap coordinate dengan matrix 
```
[[ H00, H01, H02],
 [ H10, H11, H12],
 [ H20, H21, H22]]
```
yang dimana kita dikasih kebebasan untuk mengisi setiap element matrix, untuk melakukan hal tersebut kita membutuhkan 4 coordinate awal dan 4 coordinate akhir, lalu satu coordinate awal akan di bandingkan dengan satu coordinate akhir.

