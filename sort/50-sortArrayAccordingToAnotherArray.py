'''
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will 
be same as those are in A2. For the elements not present in A2, append them at last in sorted order. 
Example: 

Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
       A2[] = {2, 1, 8, 3}
Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}
'''
def sort(A1, A2):
    d = {x : A1.count(x) for x in A1}
    k = 0
    for i in A2:
        if i in d:
            for x in range(d[i]):
                A1[k] = i
                k += 1
            d.pop(i)
    for key in sorted(d.keys()):
        for x in range(d[key]):
            A1[k] = key
            k += 1

A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
sort(A1, A2)
print(A1)