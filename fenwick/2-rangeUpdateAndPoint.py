from random import randint
from fenwick import FenwickTree

a = [0 for i in range(10)]
BIT = FenwickTree(a)
for i in range(10):
    op = randint(1, 100) % 2
    if op == 0:
        data = randint(1, 5)
        l = randint(0, len(a) - 1)
        r = randint(l, len(a) - 1)
        BIT.update(l, data)
        BIT.update(r + 1, -data)
        print(l, r, data, BIT)
    else:
        x = randint(0, len(a) - 1)
        result = BIT.getSumFromStart(x + 1)
        print(result)

[3, 8, 9, 11, 3, 5, 6, 6, 0, 0]