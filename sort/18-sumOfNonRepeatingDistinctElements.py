'''
Given an integer array with repeated elements, the task is to find sum of all distinct elements in array.
Examples: 

Input  : arr[] = {12, 10, 9, 45, 2, 10, 10, 45, 10};
Output : 78
Here we take 12, 10, 9, 45, 2 for sum
because it's distinct elements 

Input : arr[] = {1, 10, 9, 4, 2, 10, 10, 45 , 4};
Output : 71
'''
def findSum(a):
    s = set()
    sum = 0
    for i in a:
        if i not in s:
            s.add(i)
            sum += i
    return sum

a = [1, 10, 9, 4, 2, 10, 10, 45 , 4]
print(findSum(a))