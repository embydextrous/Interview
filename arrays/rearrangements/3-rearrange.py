# https://www.geeksforgeeks.org/rearrange-array-arri-arrj-even-arri/

def rearrange(a):
    copyA = a[:]
    copyA.sort()
    j = (len(a) + 1) // 2
    i = j - 1
    k = 0
    while k < len(a):
        a[k] = copyA[i]
        k += 1
        i -= 1
        if k == len(a):
            return
        a[k] = copyA[j]
        k += 1
        j += 1
    
a = [1, 2, 1, 4, 5, 6, 8, 8]
rearrange(a)
print(a)