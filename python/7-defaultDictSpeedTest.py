from collections import defaultdict
from time import perf_counter
from random import randint

TIMES = 100_000

def average_time(func):
    total = 0.0
    start = perf_counter()
    func()
    total += (perf_counter() - start) * 1e9
    return total

randoms = [randint(1, 100) for i in range(TIMES)]

def fun1():
    d = {}
    for i in randoms:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

def fun2():
    d = defaultdict(int)
    for i in randoms:
        d[i] += 1
        
dict_time = average_time(fun1)
default_dict_time = average_time(fun2)
gain = dict_time / default_dict_time
print(f"normal: {dict_time:.6} ns")
print(f"defaultdict: {default_dict_time:.6} ns  ({gain:.6}x faster)")





