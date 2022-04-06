'''
Given an unsorted array of n integers that can contain integers from 1 to n. 
Some elements can be repeated multiple times and some other elements can be absent from the array. 
Count the frequency of all elements that are present and print the missing elements.

Examples: 

Input: arr[] = {2, 3, 3, 2, 5}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 2
        3 -> 2
        4 -> 0
        5 -> 1
Explanation: Frequency of elements 1 is 
0, 2 is 2, 3 is 2, 4 is 0 and 5 is 1.
 
Input: arr[] = {4, 4, 4, 4}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 0
        3 -> 0
        4 -> 4
Explanation: Frequency of elements 1 is 
0, 2 is 0, 3 is 0 and 4 is 4.
'''
def countFreq(a):
    n = len(a)
    for i in a:
        idx = (i % (n + 1)) - 1
        a[idx] += n + 1
    print(a)
    for i in range(n):
        print("Count of " + str(i+1) + " is " + str(a[i] // (n + 1)))

a = [4, 4, 4, 4]
countFreq(a)
