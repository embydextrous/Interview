from collections import Counter
from heapq import heapify, heappop, heappush

def rearrangeCharacters(inp):
    f = Counter(inp)
    h = [[-f[key], key] for key in f.keys()]
    heapify(h)
    result = []
    lastChar = [1, "#"]
    while len(h) > 0:
        currentChar = heappop(h)
        result.append(currentChar[1])
        if lastChar[0] < 0:
            heappush(h, lastChar)
        currentChar[0] += 1
        lastChar = currentChar
    if len(inp) == len(result):
        return "".join(result)
    else:
        return "Impossible"

inp = "aabbccddee"
print(rearrangeCharacters(inp))
        