'''
You are given n activities with their start and finish times. Select the maximum number of activities 
that can be performed by a single person, assuming that a person can only work on a single activity at a time. 

How does Greedy Choice work for Activities sorted according to finish time? 
Let the given set of activities be S = {1, 2, 3, …n} and activities are sorted by finish time. 
The greedy choice is to always pick activity 1. How come activity 1 always provides one of the optimal 
solutions. We can prove it by showing that if there is another solution B with the first activity other 
than 1, then there is also a solution A of the same size with activity 1 as the first activity. 
Let the first activity selected by B be k, then there always exist A = {B - {k}} U {1}.
'''
def activitySelection(activities):
    activities.sort(key = lambda x : x[1])
    finishTime = 0
    for activity in activities:
        if activity[0] >= finishTime:
            print(activity)
            finishTime = activity[1]

activities = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
activitySelection(activities)