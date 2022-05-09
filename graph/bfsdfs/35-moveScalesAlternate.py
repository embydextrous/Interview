'''
Given a weighting scale and an array of different positive weights where we have an infinite supply of 
each weight. Our task is to put weights on left and right pans of scale one by one in such a way that 
pans move to that side where weight is put i.e. each time, pans of scale moves to alternate sides.

We are given another integer 'steps', times which we need to perform this operation.
Another constraint is that we can't put same weight consecutively i.e. if weight w is taken then in 
next step while putting the weight on opposite pan we can't take w again.

Examples:

    Let weight array is [7, 11]  and steps = 3 
    then 7, 11, 7 is the sequence in which 
    weights should be kept in order to move
    scale alternatively.

    Let another weight array is [2, 3, 5, 6] 
    and steps = 10 then, 3, 2, 3, 5, 6, 5, 3, 
    2, 3 is the sequence in which weights should
    be kept in order to move scale alternatively.
'''
def dfs(weights, stepsTaken, steps, residue, currentSteps):
    if currentSteps == steps:
        return True
    for weight in weights:
        if weight > residue and weight != stepsTaken[currentSteps - 1]:
            stepsTaken[currentSteps] = weight
            if dfs(weights, stepsTaken, steps, weight - residue, currentSteps + 1):
                return True
    return False

def printStepsToMovePanToAlternateSide(weights, steps):
    stepsTaken = [0] * steps
    residue = 0
    currentSteps = 0
    if dfs(weights, stepsTaken, steps, residue, currentSteps):
        print(stepsTaken)
    else:
        print("Not Possible")
    
steps = 10
weights = [2, 3, 5, 6]
printStepsToMovePanToAlternateSide(weights, steps)