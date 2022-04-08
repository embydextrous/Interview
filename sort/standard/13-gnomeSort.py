'''
Gnome Sort also called Stupid sort is based on the concept of a Garden Gnome sorting his flower pots. 
A garden gnome sorts the flower pots by the following method-  

He looks at the flower pot next to him and the previous one; if they are in the right order he 
steps one pot forward, otherwise he swaps them and steps one pot backwards.

If there is no previous pot (he is at the starting of the pot line), he steps forwards; 
if there is no pot next to him (he is at the end of the pot line), he is done.
'''
from random import randint

# https://www.geeksforgeeks.org/gnome-sort-a-stupid-one/
'''
Time complexity is O(N^2).
However this sorting algorithm is adaptive and performs better if the array is already/partially sorted.
'''
def gnomeSort(a):
    n = len(a)
    i = 0
    while i != n - 1:
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            i -= 1
            if i == -1:
                i = 0
        else:
            i += 1

a = [randint(1, 20) for i in range(10)]
gnomeSort(a)
print(a)