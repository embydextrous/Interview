# https://www.geeksforgeeks.org/a-product-array-puzzle/

def productArray(a):
    n = len(a)
    preProd = [1] * n
    postProd = [1] * n
    result = [0] * n
    for i in range(1, n):
        preProd[i] = preProd[i-1] * a[i-1]
    for i in range(n-2, -1, -1):
        postProd[i] = postProd[i+1] * a[i+1]
    for i in range(n):
        print(preProd[i] * postProd[i], end = " ")
    print()
    

a = [10, 3, 5, 6, 2]
productArray(a)
