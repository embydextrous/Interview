'''
We have an integer array that is sorted in ascending order. We also have 3 integers A, B and C. 
We need to apply A*x*x + B*x + C for each element x in the array and sort the modified array. 

Example: 

Input : arr[] = {-1, 0, 1, 2, 3, 4} 
       A = -1, B = 2, C = -1
Output : {-9, -4, -4, -1, -1, 0}
Input array is {-1, 0, 1, 2, 3, 4}. After
applying the equation A*x*x + B*x + C on
every element x we get, {-4,-1, 0, -1, -4, -9}
After sorting, we get {-9, -4, -4, -1, -1, 0}
'''
def sortedToEqn(a, A, B, C):
    if A == 0:
        return
    ip = (-1 * B) / (2 * A)
    n = len(a)
    result = [0] * n
    if A > 0:
        l = 0
        r = n - 1
        k = n - 1
        while l <= r:
            if abs(a[l] - ip) > abs(a[r] - ip):
                result[k] = a[l]
                l += 1
            else:
                result[k] = a[r]
                r -= 1
            k -= 1
    else:
        l = 0
        r = n - 1
        k = 0
        while l <= r:
            if abs(a[l] - ip) >= abs(a[r] - ip):
                result[k] = a[l]
                l += 1
            else:
                result[k] = a[r]
                r -= 1
            k += 1
    a[:] = result[:]


a = [-1, 0, 1, 2, 3, 4]
A = -3
B = -2
C = 4
b = []
for x in a:
    b.append(A * x * x + B * x + C)
print(b)
sortedToEqn(a, A, B, C)
print(a)





            
            
