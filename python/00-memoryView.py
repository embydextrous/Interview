from time import perf_counter
from random import randint

TIMES = 100_000

def average_time(func):
    total = 0.0
    start = perf_counter()
    func()
    total += (perf_counter() - start) * 1e9
    return total

s = ""
a = []
for i in range(TIMES):
    a.append(chr(randint(ord('a'), ord('z'))))
s = "".join(a)
randoms = [(randint(1, 100), randint(TIMES-100, TIMES)) for i in range(TIMES)]

def fun1():
    for (i, j) in randoms:
        s[i:j]

def fun2():
    mView = memoryview(s)
    for (i, j) in randoms:
        mView[i:j]
        
slice_time = average_time(fun1)
memory_view_slice_time = average_time(fun2)
gain = slice_time / memory_view_slice_time
print(f"slice time: {slice_time:.6} ns")
print(f"memory view slice time: {memory_view_slice_time:.6} ns  ({gain:.6}x faster)")





