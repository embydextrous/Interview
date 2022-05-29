from collections import defaultdict, deque
from os import pread
from typing import Counter
from unittest import result
from bst import Node, search, inorder

# 17
def check(pre):
    n = len(pre)
    if n == 0:
        return False
    s = []
    mini = -10 ** 9
    for x in pre:
        if x < mini:
            return False
        while len(s) > 0 and s[-1] < x:
            mini = s.pop()
        s.append(x)
    return True

pre = [40, 30, 35, 80, 100]
print(check(pre))
