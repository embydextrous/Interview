from collections import OrderedDict

# Similar to LinkedHashMap in Java - maintains insertion order
# Normal dict is same as HashMap in Java

'''
How to Iterate Dict
1. using key
2. using items() -> returrns list of tuple
3. using keys() -> returns list of keys
'''

'''
Python 3.6 introduced a new implementation of dict. This implementation provides an unexpected new feature: 
now regular dictionaries keep their items in the same order they're first inserted.

Still, OrderedDict is important. Why?
1. Explicitly mentions that order is important.
2. Enhanced methods.
3. Equality checks between two dictionaries.
4. Backward Compatibility
'''
d = {}
d[2] = 3
d[1] = 4
d[0] = 5
d[3] = 8
print(d)

d = OrderedDict()
d[2] = 3
d[1] = 4
d[0] = 5
d[3] = 8
print(d)
d.move_to_end(0) # Moves existing element to end - very handy for implementing LRU
d.move_to_end(0, last = False) # Moves existing element to beginning
print(d)

letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)

# Ordered dictionaries compare content and order
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)
letters_1.move_to_end("a", last = False)
letters_1.move_to_end("d")
print(letters_0 == letters_1)
letters_1.popitem() # Efficient as DLL
letters_1.popitem(last=False)


