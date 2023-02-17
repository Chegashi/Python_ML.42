from NumPyCreator import NumPyCreator

npc = NumPyCreator()

npc.from_list([[],[]])
print("Shoud Output:\narray([], shape=(2, 0), dtype=float64)\n\n")

npc.from_list([[1,2,3],[6,3,4],[8,5,6]])
print("Shoud Output:\narray([[1, 2, 3],\n\t[6, 3, 4],\n\t[8, 5, 6]])\n\n")

npc.from_tuple(("a","b","c"))
print("Shoud Output:\narray(['a', 'b', 'c'], dtype='<U1')\n\n")

npc.from_iterable(range(5))
print("Shoud Output:\narray([0, 1, 2, 3, 4])\n\n")

npc.from_shape((0, 0))
print("Shoud Output:\narray([], shape=(0, 0), dtype=float64)\n\n")

npc.from_shape((3, 5))
print("Shoud Output:\narray([[0., 0., 0., 0., 0.],\n\t[0., 0., 0., 0., 0.],\n\t[0., 0., 0., 0., 0.]])\n\n")


npc.random((3, 5))
print("Shoud Output:\narray([[0.74819604, 0.32295616, 0.27371925, 0.57171326, 0.92582071],\n\t[0.70307642, 0.94846695, 0.12465384, 0.25146454, 0.11179953],\n\t[0.38326719, 0.26179493, 0.88157011, 0.29978869, 0.72677049]])\n\n")

npc.identity(4)
print("Shoud Output:\narray([[1., 0., 0., 0.],\n\t[0., 1., 0., 0.],\n\t[0., 0., 1., 0.],\n\t[0., 0., 0., 1.]])\n\n")


print(npc.from_list("toto"))
print("Shoud Output:\nNone\n\n")

print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
print("Shoud Output:\nNone\n\n")

print(npc.from_tuple(3.2))
print("Shoud Output:\nNone\n\n")

print(npc.from_tuple(((1,5,8),(7,5))))
print("Shoud Output:\nNone\n\n")

print(npc.from_shape((-1, -1)))
print("Shoud Output:\nNone\n\n")

print(npc.identity(-1))
print("Shoud Output:\nNone\n\n")
