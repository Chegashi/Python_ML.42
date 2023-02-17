import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
print("\n#Output :\narray([[ 5],\n[10],\n[15]])\n")

print("\n__________________________________________________________________\n")

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,1))
print("#Output :\narray(\n [[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],\n[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],\n[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],\n[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],\n[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],\n[’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)")

print("\n__________________________________________________________________\n")

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
print("#Output :\narray([[1, 2, 3, 1, 2, 3, 1, 2, 3],\n[1, 2, 3, 1, 2, 3, 1, 2, 3],\n[1, 2, 3, 1, 2, 3, 1, 2, 3]])\n")
