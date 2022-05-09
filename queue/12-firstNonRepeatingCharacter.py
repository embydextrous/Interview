from collections import deque, defaultdict

def firstNonRepeatingCharacter(s):
    d = defaultdict(int)
    q = deque()
    for c in s:
        if c not in d:
            q.append(c)
        d[c] += 1
    while len(q) > 0:
        x = q.popleft()
        if d[x] == 1:
            return x
    return None

s = "narendra modi is going to win up elections with yogi adityanath"
print(firstNonRepeatingCharacter(s))
    
