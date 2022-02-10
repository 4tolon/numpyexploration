import numpy as np
# LISTA NORMAL
a = [1, 2, 3, 4, 5]
print(a)
print(a[1])
print(type(a))
# NUMPY ARRAY
b = np.array([1, 2, 3, 4, 5])
print(b)
print(b[1])
print(type(b))

mat = np.\
    array([[[1, 2, 3, 1],
            [4, 5, 6, 1],
            [7, 8, 9, 1]],
           [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]])

print(mat.shape)
print(mat.ndim)
print(mat.size)
print(mat.dtype)
print(mat)

d = np.array([[1, 2, 3],
             [4, 'hello', 6],
             [7, 8, 9]])
print(d.dtype)
print(type(d[0][0]))

siete = np.full((10, 10, 2, 2), 4)
print(siete)