'''
Given an array of an integer of size, N. Array contains N ropes of length Ropes[i]. 
You have to perform a cut operation on ropes such that all of them are reduced by the length of the 
smallest rope. Display the number of ropes left after every cut. Perform operations till the length of 
each rope becomes zero. 
Note: IF no ropes left after a single operation, in this case, we print 0. 

Examples:  

    Input : Ropes[] = { 5, 1, 1, 2, 3, 5 } 
    Output : 4 3 2 
    Explanation : In first operation the minimum ropes is 1 so we reduce length 1 from all of them after 
    reducing we left with 4 ropes and we do same for rest.

    Input : Ropes[] = { 5, 1, 6, 9, 8, 11, 2, 2, 6, 5 } 
    # 1 2 2 5 5 6 6 8 9 11
    Output : 9 7 5 3 2 1 

'''
def ropesLeft(a):
    a.sort()
    n = len(a)
    i = 0
    while i < n:
        if i + 1 < n and a[i] != a[i+1]:
            print(n - i - 1, end = " ")
        i += 1
    print()

a = [5, 1, 6, 9, 8, 11, 2, 2, 6, 5]
ropesLeft(a)
    
