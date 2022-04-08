'''
Given an array A positive integers, sort the array in ascending order such that element in given 
subarray (start and end indexes are input) in unsorted array stay unmoved and all other elements are sorted.
Examples : 

Input : arr[] = {10, 4, 11, 7, 6, 20}
            l = 1, u = 3
# 4 6 7 10 11 20
Output : arr[] = {6, 4, 11, 7, 10, 20}
We sort elements except arr[1..3] which
is {11, 7, 6}. 

Input : arr[] = {5, 4, 3, 12, 14, 9};
            l = 1, u = 2;
Output : arr[] = {5, 4, 3, 9, 12, 14 }
We sort elements except arr[1..2] which
is {4, 3}. 
'''
def sort(a, l, r):
    copy = []
    for i in range(len(a)):
        if i < l or i > r:
            copy.append(a[i])
    copy.sort()
    j = 0
    for i in range(len(a)):
        if i < l or i > r:
            a[i] = copy[j]
            j += 1

a = [5, 4, 3, 12, 14, 9]
l, r = 1, 2
sort(a, l, r)
print(a)