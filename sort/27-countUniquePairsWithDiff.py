'''
Given an integer array and a positive integer k, count all distinct pairs with differences equal to k. 

Examples: 

Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2} 

Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
Output: 5
There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, 
{8, 12}, {12, 16} and {16, 20} 
'''
def countPairs(a, x):
    a.sort()
    i, j = 0, 1
    c = 0
    while j < len(a):
        if a[j] - a[i] == x:
            c += 1
            j += 1
            while j < len(a) and a[j] == a[j-1]:
                j += 1
        elif a[j] - a[i] < x:
            j += 1
            while j < len(a) and a[j] == a[j-1]:
                j += 1
        else:
            i += 1
            while i < j and a[i] == a[i-1]:
                i += 1
    return c

def countPairs2(a, x):
    a.sort()
    i, j = 0, 1
    c = 0
    s = set()
    while j < len(a):
        if a[j] - a[i] == x:
            if (a[i], a[j]) not in s:
                s.add((a[i], a[j]))
                c += 1
            j += 1
        elif a[j] - a[i] < x:
            j += 1
        else:
            i += 1
    return c

a = [1, 2, 3, 4, 5]
x = 3
print(countPairs(a, x))

