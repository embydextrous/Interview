'''
giveGiven an array of N integers with duplicates allowed. All elements are ranked from 1 to N in ascending order if they are distinct. If there are say x repeated elements of a particular value then each element should be assigned a rank equal to the arithmetic mean of x consecutive ranks.
Examples: 
 

Input : 20 30 10
Output : 2.0 3.0 1.0

Input : 10 12 15 12 10 25 12
Output : 1.5, 4.0, 6.0, 4.0, 1.5, 7.0, 4.0
'''
def rankify(a):
    n = len(a)
    rankArray = []
    for i in range(n):
        rankArray.append([a[i], i])
    rankArray.sort(key = lambda x : x[0])
    i = 0
    while i < n - 1:
        c = 1
        j = i
        while j < n - 1 and rankArray[j][0] == rankArray[j+1][0]:
            c += 1
            j += 1
        for k in range(i, j + 1):
            rank = ((j + 2) * (j + 1) / 2 - (i + 1) * i / 2) / (j - i + 1)
            rankArray[k][0] = rank
        i = j + 1
    if rankArray[n-1][0] != rankArray[n-2][0]:
        rankArray[n-1][0] = n / 1.0
    rankArray.sort(key = lambda x : x[1])
    for i in range(n):
        print(rankArray[i][0], end = " ")
    print()
    

a = [10, 12, 25, 12, 10, 25, 12]
rankify(a)

        
