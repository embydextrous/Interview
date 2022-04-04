# https://www.geeksforgeeks.org/find-whether-possible-make-array-elements-using-one-external-number/

def isPossible(a):
    count = 0 # Unique count
    s = set()
    sum = 0
    for i in a:
        if i in s:
            continue
        s.add(i)
        count += 1
        sum += i
        if count == 4:
            return False
    if count <= 2:
        return True
    a, c = min(s), max(s)
    b = sum - a - c
    return b - a == c - b

a = [1, 9, 9, 5, 1, 5, 5, 1, 5, 1, 9, 4]
print(isPossible(a))
    
    
