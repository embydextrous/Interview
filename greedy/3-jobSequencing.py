'''
Given an array of jobs where every job has a deadline and associated profit if the job is finished 
before the deadline. It is also given that every job takes a single unit of time, so the minimum 
possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.

Examples: 

Input: Four Jobs with following 
deadlines and profits
JobID  Deadline  Profit
  a      4        20   
  b      1        10
  c      1        40  
  d      1        30
Output: Following is maximum 
profit sequence of jobs
        c, a   


Input:  Five Jobs with following
deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: Following is maximum 
profit sequence of jobs
        c, a, e
'''
import heapq

def maxProfit(jobs):
    jobs.sort(key = lambda x : x[2], reverse = True)
    result = [None] * len(jobs)
    profit = 0
    for job in jobs:
        deadline = job[1]
        for i in range(deadline - 1, -1, -1):
            if result[i] == None:
                result[i] = job
                profit += job[2]
                break
    return (profit, result)

def maxProfitOptimized(jobs):
    n = len(jobs)
    jobs.sort(key = lambda x : x[1])
    result = []
    maxHeap = []
    maxProfit = 0
    print(jobs)
    for i in range(n - 1, -1, -1):
        if i == 0:
            slots_available = jobs[i][1]
        else:
            slots_available = jobs[i][1] - jobs[i - 1][1]
        heapq.heappush(maxHeap, (-jobs[i][2], jobs[i][1], jobs[i][0]))
        while slots_available > 0 and len(maxHeap) > 0:
            profit, deadline, job_id = heapq.heappop(maxHeap)
            maxProfit += profit
            slots_available -= 1
            result.append([job_id, deadline, profit * -1])
    result.sort(key=lambda x: x[1])
    return (maxProfit * -1, result)

jobs = [['b', 1, 19], ['d', 1, 25], ['a', 3, 100], ['e', 3, 15], ['c', 3, 27]]
print(maxProfitOptimized(jobs))