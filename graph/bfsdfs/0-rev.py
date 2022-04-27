from collections import defaultdict, deque
from email.policy import default

def steppingNumbers(n):
    if n <= 10:
        return [i for i in range(n)]
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result = []
    result.extend([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    i = 10
    while i != n:
        x = q.popleft()
        if x % 10 != 0:
            result.append(10 * x + (x % 10 - 1))
            q.append(10 * x + (x % 10 - 1))
            i += 1
            if i == n:
                break
        if x % 10 != 9:
            result.append(10 * x + (x % 10 + 1))
            q.append(10 * x + (x % 10 + 1))
            i += 1
    return result

            
print(steppingNumbers(50))
