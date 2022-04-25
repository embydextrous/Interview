from collections import ChainMap, defaultdict

'''
Python's ChainMap was added to collections in Python 3.3 as a handy tool for managing multiple scopes
and contexts. This class allows you to group several dictionaries and other mappings together to make
them logically appear and behave as one. It creates a single updatable view that works similar to a 
regular dictionary but with some internal differences.
'''

d = {1:1, 2:2, 3:3}
d2 = defaultdict()
d2["one"] = 1
d2["two"] = 2
d2["three"] = 3
chainMap = ChainMap(d, d2)
print(chainMap)
# ChainMap({1: 1, 2: 2, 3: 3}, defaultdict(None, {'one': 1, 'two': 2, 'three': 3}))
# Mappings are not merged but kept as list of mappings.

'''
When you're working with ChainMap, you can chain several dictionaries with keys that are either disjoint
or intersecting.

In the first case, ChainMap allows you to treat all your dictionaries as one. So, you can access the 
key-value pairs as if you were working with a single dictionary. In the second case, besides managing 
your dictionaries as one, you can also take advantage of the internal list of mappings to define some 
sort of access priority for repeated keys across your dictionaries. That's why ChainMap objects are 
great for handling multiple contexts.
'''

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)
pets["dogs"] #10, first Value
pets.get("cats") #7
pets["turtles"] #1

print(pets.keys())
# KeysView(ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'cats': 3, 'turtles': 1}))
print(pets.items())
# ItemsView(ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'cats': 3, 'turtles': 1}))


# Chaining vs Merging
for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)
print(pets)
# ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'cats': 3, 'turtles': 1})
pets = {}
pets.update(for_adoption)
pets.update(vet_treatment)
print(pets)
# {'dogs': 4, 'cats': 3, 'pythons': 3, 'turtles': 1}
'''
Now suppose you have n different mappings with at most m keys each. Creating a ChainMap object from them
would take O(n) execution time, while retrieving a key would take O(n) in the worst-case scenario, in which
the target key is in the last dictionary of the internal list of mappings.

Alternatively, creating a regular dictionary using .update() in a loop would take O(nm), while retrieving
a key from the final dictionary would take O(1).
'''

# maps
for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)
print(pets.maps) # gives list of mappings that can be manipulated
print(pets)
# ChainMap({'dogs': 10, 'cats': 7, 'pythons': 3}, {'dogs': 4, 'cats': 3, 'turtles': 1})
pets.maps.reverse()
print(pets)
# ChainMap({'dogs': 4, 'cats': 3, 'turtles': 1}, {'dogs': 10, 'cats': 7, 'pythons': 3})

# parents
print(pets.parents) # returns new chainmap with first mapping removed

# new_child
pets = pets.new_child({"one": 1})
print(pets)