'''
Given an array arr that has numbers appearing twice or once.
The task is to identify numbers that occurred only once in the array.
Note: Duplicates appear side by side every time. Might be few numbers can occur one time and just assume this is a 
right rotating array (just say an array can rotate k times towards right). 
Order of the elements in the output doesn't matter.
Examples:
Input: arr[] = { 7, 7, 8, 8, 9, 1, 1, 4, 2, 2 }
Output: 9 4
Input: arr[] = {-9, -8, 4, 4, 5, 5, -1}
Output: -9 -8 -1
'''
def printElementsThatAppearOnlyOnce(a):
    n = len(a)
    if a[0] == a[-1]:
        i = 1
    else:
        i = 0
    while i < n:
        if i == n - 1:
            print(a[i], end = " ")
            break
        elif a[i] != a[i+1]:
            print(a[i], end = " ")
            i += 1
        else:
            i += 2
    print()

a = [7, 7, 8, 8, 9, 1, 1, 4, 2, 2]
printElementsThatAppearOnlyOnce(a)
        