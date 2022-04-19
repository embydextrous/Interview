from collections import defaultdict, Counter
from time import perf_counter
from random import randint

TIMES = 1_000_000

def average_time(func):
    total = 0.0
    start = perf_counter()
    func()
    total += (perf_counter() - start) * 1e3
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

def fun3():
    d = {x : randoms.count(x) for x in randoms }

def fun4():
    Counter(randoms)
        
dict_time = average_time(fun1)
default_dict_time = average_time(fun2)
#lambds_shorthand_time = average_time(fun3)
counter_time = average_time(fun4)

gain1 = dict_time / default_dict_time
#gain2 = dict_time / lambds_shorthand_time
gain3 = dict_time / counter_time

print(f"normal: {dict_time:.6} ms")
print(f"defaultdict: {default_dict_time:.6} ns  ({gain1:.6}x faster)")
# print(f"lamnda shorthand: {lambds_shorthand_time:.6} ms  ({gain2:.6}x faster)")
print(f"counter: {counter_time:.6} ms  ({gain3:.6}x faster)")






