from collections import defaultdict
from email.policy import default

# Problem with {} is missing keys. Let's see it while implementing counter
a = [1, 1, 2, 2, 3, 3, 4]
d = {}
'''
for i in a:
    d[i] += 1   // Gives KeyError if key does not exist
print(d)
'''
# To solve above problem you can do this
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

# But that is not so pythonic, one thing we can do is to use get() function
d = {}
for i in a:
    d[i] = d.get(i, 0) + 1
print(d)

def defValue():
    return 0
# But there can be other cases where you might require some different default implementation. We will see
# one example later. But, let's see how to resolve this using defaultdict
d = defaultdict(int)
for i in a:
    d[i] += 1

# You can use any callable here - actually you are using int() in this case
def defValue():
    return 0

d = defaultdict(defValue)
for i in a:
    d[i] += 1

# Grouping Case
pets = [("dog", "Affenpinscher"), ("dog", "Terrier"), ("dog", "Boxer"), ("cat", "Abyssinian"), ("cat", "Birman")]
d = defaultdict(list)
for (pet, breed) in pets:
    d[pet].append(breed)

print(d)