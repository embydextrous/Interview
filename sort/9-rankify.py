'''
giveGiven an array of N integers with duplicates allowed. All elements are ranked from 1 to N in ascending order if they are distinct. If there are say x repeated elements of a particular value then each element should be assigned a rank equal to the arithmetic mean of x consecutive ranks.
Examples: 
 

Input : 20 30 10
Output : 2.0 3.0 1.0

Input : 10 12 15 12 10 25 12
Output : 1.5, 4.0, 6.0, 4.0, 1.5, 7.0, 4.0
'''
def rankify(a):
    sortedA = sorted(a)
    d = {}
    for i in range(len(sortedA)):
        x = sortedA[i]
        if x not in d:
            d[x] = [i + 1, i + 1]
        else:
            d[x][1] = i + 1
    for i in a:
        n = d[i][1] - d[i][0] + 1
        s = (d[i][1] * (d[i][1] + 1)) // 2 - (d[i][0] * (d[i][0] - 1)) // 2
        print(s / n, end = " ")
    print()
    

a = [10, 12, 25, 12, 10, 25, 12]
rankify(a)

        
