'''
We are given N jobs numbered 1 to N. For each activity, let Ti denotes the number of days required 
to complete the job. For each day of delay before starting to work for job i, a loss of Li is incurred.
We are required to find a sequence to complete the jobs so that overall loss is minimized. 
We can only work on one job at a time.

Input : L = {3, 1, 2, 4} and 
        T = {4, 1000, 2, 5}
Output : 3, 4, 1, 2
Explanation: We should first complete 
job 3, then jobs 4, 1, 2 respectively.

Input : L = {1, 2, 3, 5, 6} 
        T = {2, 4, 1, 3, 2}
Output : 3, 5, 4, 1, 2 
Explanation: We should complete jobs 
3, 5, 4, 1 and then 2 in this order.
'''
class Job:
    def __init__(self, days, loss):
        self.days = days
        self.loss = loss

    def __le__(self, other):
        return self.loss * other.days <= other.loss * self.days
    
    def __lt__(self, other):
        return self.loss * other.days < other.loss * self.days

    def __repr__(self):
        return "Job({},{})".format(self.days, self.loss)

def schedule(jobs):
    jobs.sort(reverse = True)
    return jobs

jobs = [Job(2, 1), Job(4, 2), Job(1, 3), Job(3, 5), Job(2, 6)]
print(schedule(jobs))

