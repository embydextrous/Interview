'''
In Python, append and pop operations on the beginning or left side of list objects are inefficient, with O(n) 
time complexity. These operations are especially expensive if you're working with large lists because Python 
has to move all the items to the right to insert new items at the beginning of the list.

On the other hand, append and pop operations on the right side of a list are normally efficient (O(1)) except 
for those cases in which Python needs to reallocate memory to grow the underlying list for accepting new items.

Python's deque was created to overcome this problem. Append and pop operations on both sides of a deque object 
are stable and equally efficient because deques are implemented as a doubly linked list. That's why deques are 
particularly useful for creating stacks and queues.

# Normal lists are good to be used as stacks but not as queues. However, better to use deque if you require stack
or queue as it gives API intuition.
'''
# https://realpython.com/python-deque/
from collections import deque
# append and pop operations are thread safe
# As Queue
q = deque()
q.append(1)
q.append(2)
q.append(3)
# print(len(q)) - Yes you can use len. For peek use indexes as complecity of index access at ends is O(1)
print(q.popleft())
print(q.popleft())
print(q.popleft())

# As Stack
s = deque()
s.append(1)
s.append(2)
s.append(3)
print(s.pop())
print(s.pop())
print(s.pop())

# Insert left and init
# Once the deque reaches its maximum size, adding a new item on an end of the deque automatically discards
# the item at the opposite end. If you don’t supply a value to maxlen, then the deque can grow to an 
# arbitrary number of items.
a = deque(["Maidy", "Madu", "Modu"], maxlen=4)
a.appendleft("Middi")
print(a)

# Deque from Tuple
a = deque((1, 2, 3, 4))
print(a)

# Deque from List
a = deque([1, 2, 3, 4])
print(a)

# Deque from String
a = deque("1234")
print(a)

# a.pop(2) - deque does not support removal from anywhere like lists

# extend a deque
a = deque([1, 2, 3, 4])
print(a)
a.extend([5, 6, 7]) # 5 is appended to right first then 6 and then 7
print(a)
a.extendleft([0, 8]) # 0 is appended to left first then 8
print(a)
a.rotate(1) # Right rotates, for left use -ve
print(a)

# Indices can be used to access elements of a deque but you cannot slice it.
'''
deque are implemented a little smarter than just doubly-linked lists. They're a doubly-linked list of blocks
of Python objects, where the left and right sides may be incomplete blocks.

The Big-O cost of accessing in the middle is still O(n), but it has a constant divisor (implementation dependent,
CPython 3.5 allocates blocks that can store 64 objects). So if your deque has 1000 members, accessing in the 
middle still involves only around 7-8 "linked list-style" traversals, not 500-some. If the deque is smallish 
(65 to 128 elements, depending on how the empty slots align with the head and tail blocks), then lookup of any 
element is equal cost.
'''
b = a.copy()
b.popleft()
print(a)
print(b)

# Other methods
# remove(a) -> removes first occurence in O(n) but is faster than list
# count(x) -> returns count of x in O(n)
# clear() -> clears deque
print()
a.remove(2)
print(a)
print(a.count(3))
a.clear()
print(a)