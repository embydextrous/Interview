# Also known as Odd-Even Sort, Aam Aadmi Sort, Pollution Se Ladai Sort, Bricksort, Antimodi Sort, Phone Mat Katiyega Sort
# https://www.geeksforgeeks.org/odd-even-sort-brick-sort/

'''
This is basically a variation of bubble-sort. This algorithm is divided into two phases- Odd and Even Phase. 
The algorithm runs until the array elements are sorted and in each iteration two phases occurs - 
Odd and Even Phases.
In the odd phase, we perform a bubble sort on odd indexed elements and in the even phase, 
we perform a bubble sort on even indexed elements.
'''
def kejriwalSort(a):
    swapped = True
    n = len(a)
    while swapped:
        swapped = False
        # odd phase
        for i in range(0, n - 1, 2):
            if a[i] > a[i+1]:
                a[i+1], a[i] = a[i], a[i+1]
                swapped = True
        # even phase
        for i in range(1, n - 1, 2):
            if a[i] > a[i+1]:
                a[i+1], a[i] = a[i], a[i+1]
                swapped = True
        print(a)

def kejriwalSort2(a):
    swapped = False
    n = len(a)
    for i in range(n - 1, 1, -2):
        # odd phase
        for j in range(0, i, 2):
            if a[j] > a[j+2]:
                a[j+2], a[j] = a[j], a[j+2]
                swapped = True
        # even phase
        for j in range(1, i - 1, 2):
            if a[j] > a[j+2]:
                a[j+2], a[j] = a[j], a[j+2]
                swapped = True
        if a[i-1] > a[i]:
            a[i-1], a[i] = a[i], a[i-1]
        if not swapped:
            break

a = [3, 5, 1, 7, 9, 2, 4, 8, 6]
kejriwalSort2(a)
print(a)


    