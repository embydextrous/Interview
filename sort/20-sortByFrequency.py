'''
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency 
then print the one which came first. 

Examples:  

Input:  arr[] = {5, 2, 5, 8, 2, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
'''
def sortByFreq(a):
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]][0] += 1
        else:
            d[a[i]] = [1, i]
    a.sort(key = lambda x : (-d[x][0], d[x][1]))

a = [2, 5, 5, 8, 2, 6, 8, 8]
sortByFreq(a)
print(a)