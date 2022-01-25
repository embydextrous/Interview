# https://www.geeksforgeeks.org/find-elements-array-least-two-greater-elements/
import sys

# Find second largest element
# Print all elements smaller than it
def printElements(a):
    maxi, secMaxi = -sys.maxsize-1, -sys.maxsize-1
    for i in a:
        if i >= maxi:
            maxi, secMaxi = i, maxi
        elif i> secMaxi:
            secMaxi = i
    for i in a:
        if i < secMaxi:
            print(i, end = " ")
    print()

a = [7, -2, 3, 4, 9, -1]
printElements(a)
