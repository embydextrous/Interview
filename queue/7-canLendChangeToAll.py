# https://www.geeksforgeeks.org/check-if-x-can-give-change-to-every-person-in-the-queue/

def checkChange(q):
    c5 = c10 = 0
    while len(q) > 0:
        x = q.pop(0)
        if x == 5:
            c5 += 1
        elif x == 10:
            if c5 == 0:
                return False
            c5 -= 1
            c10 += 1
        else:
            if c5 > 0 and c10 > 0:
                c5 -= 1
                c10 -= 1
            elif c5 >= 3:
                c5 -= 3
            else:
                return False
    return True


q = [5, 10, 10, 20]
print(checkChange(q))