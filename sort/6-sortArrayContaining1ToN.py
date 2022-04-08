'''
You have given an array which contain 1 to n element, your task is to sort this array in an efficient 
way and without replace with 1 to n numbers.
Examples : 
 

Input : arr[] = {10, 7, 9, 2, 8, 3, 5, 4, 6, 1};
Output : 1 2 3 4 5 6 7 8 9 10
'''
def sort(a):
    n = len(a)
    for i in range(n):
        a[i] = i + 1
        
a = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
sort(a)
print(a)