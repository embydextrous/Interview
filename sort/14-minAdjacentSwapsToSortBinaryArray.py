'''
Given a binary array, task is to sort this binary array using minimum swaps. 
We are allowed to swap only adjacent elements

Examples: 

Input : [0, 0, 1, 0, 1, 0, 1, 1]
Output : 3
1st swap : [0, 0, 1, 0, 0, 1, 1, 1]
2nd swap : [0, 0, 0, 1, 0, 1, 1, 1]
3rd swap : [0, 0, 0, 0, 1, 1, 1, 1]

Input : Array = [0, 1, 0, 1, 0]
Output : 3
'''
def count(a):
    zeroesTillNow = 0
    result = 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            zeroesTillNow += 1
        else:
            result += zeroesTillNow
    return result

a = [0, 0, 1, 0, 1, 0, 1, 0]
print(count(a))