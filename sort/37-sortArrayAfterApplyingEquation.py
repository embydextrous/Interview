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
    n = len(a)
    result = []
    minIndex = 0
    maxIndex = 0
    for i in range(n):
        a[i] = A * a[i] ** 2 + B * a[i] + C
        if a[i] < a[minIndex]:
            minIndex = i
        if a[i] > a[maxIndex]:
            maxIndex = i
    i = minIndex if A >= 0 else maxIndex
    j = i + 1
    if A >= 0:
        while i >= 0 and j < n:
            if a[i] <= a[j]:
                result.append(a[i])
                i -= 1
            else:
                result.append(a[j])
                j += 1
        while i >= 0:
            result.append(a[i])
            i -= 1
        while j < n:
            result.append(a[j])
            j += 1
    else:
        k = n - 1
        result = [0] * n
        while i >= 0 and j < n:
            if a[i] >= a[j]:
                result[k] = a[i]
                i -= 1
            else:
                result[k] = a[j]
                j += 1
            k -= 1
        while i >= 0:
            result[k] = a[i]
            i -= 1
            k -= 1
        while j < n:
            result[k] = a[j]
            j += 1
            k -= 1
    return result

a = [-1, 0, 1, 2, 3, 4]
b = a[:]
A = 2
B = 2
C = 2
print(sortedToEqn(a, A, B, C))



            
            
