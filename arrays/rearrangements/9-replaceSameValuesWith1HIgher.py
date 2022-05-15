'''
You are given an array of size 'n'. You have to replace every pair of consecutive values 'x' by a single 
value 'x+1' every time until there is no such repetition left and then print the new array.
 

    Input : 5, 2, 1, 1, 2, 2 
    Output : 5 4 
    Explanation: 
    step 1: While traversing, encountered pair of 1(gets replaced by 2. We get 5, 2, 2, 2, 2 
    step 2: The first encountered pair of 2 gets replaced by 3. We get 5, 3, 2, 2 
    step 3: Again pair of 2 gets replaced by 3. We get 5, 3, 3 
    step 4: Recently formed pair of 3 gets replaced by 4. We get 5, 4 
    This is our required answer.
    Input : 4, 5, 11, 2, 5, 7, 2 
    Output : 4 5 11 2 5 7 2
'''
def replace(a):
    s = []
    for x in a:
        if len(s) == 0 or s[-1] != x:
            s.append(x)
        else:
            while len(s) > 0 and s[-1] == x:
                s.pop()
                x = x + 1
            s.append(x)
    print(s)

a = [4, 5, 11, 2, 5, 7, 2]
replace(a)
