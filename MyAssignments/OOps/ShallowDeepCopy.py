import copy

# Shallow Copy:
a= [[1,2],[3,4]]
b = copy.copy(a)
print(b[0][0])
b[0][0] = 999
print(f"Changed value of b is {b}")
print(f"Changed value of a is {a}")
# Deep Copy:
c = [[1, 2], [3, 4]]
d = copy.deepcopy(a)
d[0][0] = 999
print(f"Changed value of c is {c}")
print(f"Changed value of d is {d}")
