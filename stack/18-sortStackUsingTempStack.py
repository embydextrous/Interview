# Also see https://www.geeksforgeeks.org/sorting-array-using-stacks/

def sort(s):
    ts = []
    while len(s) > 0:
        v = s.pop()
        if len(ts) == 0 or ts[len(ts) - 1] <= v:
            ts.append(v)
        else:
            while len(ts) > 0 and ts[len(ts) - 1] > v:
                r = ts.pop()
                s.append(r)
            ts.append(v)
    return ts
    
a = [3, 5, 1, 4, 2, 8]
print(sort(a))