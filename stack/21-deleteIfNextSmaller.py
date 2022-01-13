# https://www.geeksforgeeks.org/delete-array-elements-which-are-smaller-than-next-or-become-smaller/

def deleteIfNextSmaller(a):
    s = [a[0]]
    for i in range(1, len(a)):
        if s[len(s) - 1] < a[i]:
            while len(s) > 0 and s[len(s) - 1] < a[i]:
                s.pop()
        s.append(a[i])
    return s

a = [23, 45, 11, 77, 18]
print(deleteIfNextSmaller(a))
