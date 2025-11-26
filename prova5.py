a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1, 2, 1, 3, 5]
b = set(a)
c = list()
for e in b:
    c.append([e,a.count(e)])
print(c)
"""
a=(1, 2, 3, 1, 2, 3, 1, 4)
b = a.index(1,4)
print(b)
"""