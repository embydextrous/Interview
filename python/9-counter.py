# Counter using dictionaries
from collections import defaultdict
from collections import Counter # Subclass of dict

word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)

counter = defaultdict(int)
for letter in word:
    counter[letter] += 1

print(counter)

counter = Counter("mississippi") # Can use string, iterable, tuple - elements should be hashable
print(counter)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Update the counts of m and i - In case of counter update value is added to existing
counter.update(m=3, i=4)
print(counter)
# Counter({'i': 8, 'm': 4, 's': 4, 'p': 2})

# enter a ney key count pair
counter.update({"a": 2})
print(counter)
# Counter({'i': 8, 'm': 4, 's': 4, 'p': 2, 'a': 2})

# Update with another counter
counter.update(Counter("missouri"))
print(counter)
# Counter({'i': 10, 's': 6, 'm': 5, 'p': 2, 'a': 2, 'o': 1, 'u': 1, 'r': 1})
