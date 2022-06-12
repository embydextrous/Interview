'''
A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j 
and x[i] < x[j]. The surpasser count of an element is the number of surpassers. Given an array of distinct integers, 
for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater
than that element.
Examples : 
 
Input:  [2, 7, 5, 3, 0, 8, 1]
Output: [4, 1, 1, 1, 2, 0, 0]
'''
def surpasserCount(a, l, r, surpasser):
    if l == r:
        return
    m = l + (r - l) // 2
    surpasserCount(a, l, m, surpasser)
    surpasserCount(a, m + 1, r, surpasser)
    merge(a, l, m, r)

def merge(a, l, m, r):
    temp = [a[i] for i in range(l, r + 1)]
    i = 0
    j = m - l + 1
    k = l
    while i < m - l + 1 and j < r - l + 1:
        if temp[i][0] < temp[j][0]:
            surpasser[temp[i][1]] += r - l + 1 - j
            a[k] = temp[i]
            i += 1
        else:
            a[k] = temp[j]
            j += 1
        k += 1
    while i < m - l + 1:
        a[k] = temp[i]
        i += 1
        k += 1
    while j < r - m + 1:
        a[k] = temp[j]
        j += 1
        k += 1


a = [2, 7, 5, 3, 0, 8, 1]
n = len(a)
surpasser = [0] * n
aux = [[a[i], i] for i in range(n)]
print(surpasserCount(aux, 0, len(a) - 1, surpasser))
print(surpasser)
    
