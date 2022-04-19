# Array consists of rotation of strings
'''
Given n strings that are permutations of each other. We need to make all strings same with an operation 
that takes front character of any string and moves it to the end.
Examples: 
 
Input : n = 2
        arr[] = {"molzv", "lzvmo"}
Output : 2
Explanation: In first string, we remove
first element("m") from first string and 
append it end. Then we move second character
of first string and move it to end. So after
2 operations, both strings become same.

Input : n = 3
        arr[] = {"kc", "kc", "kc"}
Output : 0
Explanation: already all strings are equal.

 
'''
import sys

def minMoves(a):
    n = len(a[0])
    miniMoves = sys.maxsize
    for target in a:
        b = target + target
        count = 0
        for s in a:
            for i in range(n):
                if b[i:i+n] == s:
                    if i != 0:
                        count += (n - i)
                    break
        miniMoves = min(count, miniMoves)
    return miniMoves

a = ["xzzwo", "zwoxz", "zzwox", "xzzwo"]
print(minMoves(a))