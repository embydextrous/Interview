def firstNonRepeatingCharacter(s):
    d = {}
    q = []
    for c in s:
        if c not in d:
            d[c] = 1
            q.append(c)
        else:
            d[c] += 1
    while len(q) > 0:
        x = q.pop(0)
        if d[x] == 1:
            return x
    return None

s = "narendra modi is going to win up elections with yogi adityanath"
print(firstNonRepeatingCharacter(s))
    
