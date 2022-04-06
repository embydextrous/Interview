'''
Given an unsorted array that may contain duplicates. Also given a number k 
which is smaller than size of array. Write a function that returns true if 
array contains duplicates within k distance.
Examples: 

Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
Output: false
All duplicates are more than k distance away.

Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
Output: true
1 is repeated at distance 3.

Input: k = 3, arr[] = {1, 2, 3, 4, 5}
Output: false

Input: k = 3, arr[] = {1, 2, 3, 4, 4}
Output: true
'''
def check(a, k):
    n = len(a)
    s = set()
    for i in range(k + 1):
        if a[i] in s:
            return True
        s.add(a[i])
    for i in range(k + 1, n):
        print(s, a[i-k-1], a[i])
        s.remove(a[i-k-1])
        if a[i] in s:
            return True
        s.add(a[i])
    return False

a = [1, 2, 3, 4, 5]
print(check(a, 3))