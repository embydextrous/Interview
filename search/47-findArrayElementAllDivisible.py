'''
Given an array of numbers, find the number among them such that all numbers are divisible by it. 
If not possible print -1.
Examples: 
 

Input : arr = {25, 20, 5, 10, 100} 
Output : 5 
Explanation : 5 is an array element
 which divides all numbers.

Input : arr = {9, 3, 6, 2, 15} 
Output : -1 
Explanation : No numbers are divisible
by any array element.
'''
def find(a):
    x = min(a)
    for i in a:
        if i % x != 0:
            return -1
    return x

a = [9, 3, 6, 2, 15]
print(find(a))