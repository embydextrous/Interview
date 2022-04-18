from collections import deque
from time import perf_counter
from random import randint

TIMES = 10_000
a_list = []
a_deque = deque()

def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    return total / times

# Append Right - Almost Similar
list_append_time = average_time(lambda i: a_list.append(i), TIMES)
deque_append_time = average_time(lambda i: a_deque.append(i), TIMES)
gain = list_append_time / deque_append_time
print(f"list.append(): {list_append_time:.6} ns")
print(f"deque.append(): {deque_append_time:.6} ns  ({gain:.6}x faster)")

# Pop Right - Almost Similar
list_pop_time = average_time(lambda i: a_list.pop(), TIMES)
deque_pop_time = average_time(lambda i: a_deque.pop(), TIMES)
gain = list_pop_time / deque_pop_time
print(f"list.pop(): {list_pop_time:.6} ns")
print(f"deque.pop(): {deque_pop_time:.6} ns  ({gain:.6}x faster)")

# Append Left - Almost Similar
list_append_left_time = average_time(lambda i: a_list.insert(0, i), TIMES)
deque_append_left_time = average_time(lambda i: a_deque.appendleft(i), TIMES)
gain = list_append_left_time / deque_append_left_time
print(f"list.insert(): {list_append_left_time:.6} ns")
print(f"deque.appendleft(): {deque_append_left_time:.6} ns  ({gain:.6}x faster)")

# Pop Left - Almost Similar
list_pop_left_time = average_time(lambda i: a_list.pop(0), TIMES)
deque_pop_left_time = average_time(lambda i: a_deque.popleft(), TIMES)
gain = list_pop_left_time / deque_pop_left_time
print(f"list.pop(0): {list_pop_left_time:.6} ns")
print(f"deque.popleft(): {deque_pop_left_time:.6} ns  ({gain:.6}x faster)")


for i in range(TIMES):
    a_list.append(i)
    a_deque.append(i)

randoms = [randint(0, TIMES - 1) for i in range(TIMES)]

def average_access_time(func, times):
    total = 0.0
    for i in randoms:
        start = perf_counter()
        try:
            func(i)
        except:
            "aaa"
        total += (perf_counter() - start) * 1e9
    return total / times

# Random Access
list_random_access_time = average_time(lambda i: a_list[i], TIMES)
deque_random_access_time = average_time(lambda i: a_deque[i], TIMES)
gain = list_random_access_time / deque_random_access_time
print(f"list[]: {list_random_access_time:.6} ns")
print(f"deque[]: {deque_random_access_time:.6} ns  ({gain:.6}x faster)")

randoms = [randint(0, TIMES - 1) for i in range(TIMES//10)]
# in operator
list_membership_time = average_time(lambda i: i in a_list, TIMES)
deque_membership_time = average_time(lambda i: i in a_deque, TIMES)
gain = list_membership_time / deque_membership_time
print(f"i in list: {list_membership_time:.6} ns")
print(f"i in deque: {deque_membership_time:.6} ns  ({gain:.6}x faster)")

# remove operator - Deque removes is faster (may be due to block implementation)
list_remove_time = average_time(lambda i: a_list.remove(i), TIMES)
deque_remove_time = average_time(lambda i: a_deque.remove(i), TIMES)
gain = list_remove_time / deque_remove_time
print(f"list.remove(i): {list_remove_time:.6} ns")
print(f"deque.remove(i): {deque_remove_time:.6} ns  ({gain:.6}x faster)")