# O(n^2) solution. Can be optimized to O(n) using Booth's Algorithm
'''
Write code to find lexicographic minimum in a circular array, e.g. for the array BCABDADAB, 
the lexicographic minimum is ABBCABDAD.
Source: Google Written Test
More Examples: 

Input:  GEEKSQUIZ
Output: EEKSQUIZG

Input:  GFG
Output: FGG

Input:  GEEKSFORGEEKS
Output: EEKSFORGEEKSG
'''
def lexicoGraphicallyLowestRotation(s):
    n = len(s)
    lowest = s
    s += s
    for i in range(1, n):
        for j in range(n):
            if ord(lowest[j]) > ord(s[i + j]):
                lowest = s[i:i+n]
            elif ord(lowest[j]) < ord(s[i + j]):
                break
    return lowest

s = "modi"
print(lexicoGraphicallyLowestRotation(s))

