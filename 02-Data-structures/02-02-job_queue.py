# python2
#Task. You have a program which is parallelized and uses  independent threads to process the given list
#of m jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
#it immediately takes the next job from the list. If a thread has started processing a job, it doesn
#interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
#simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
#will it take any thread to process this job, and this time is the same for all the threads. You need to
#determine for each job which thread will process it and when will it start processing.

import Queue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, raw_input().split())
        self.jobs = list(map(int, raw_input().split()))
        assert m == len(self.jobs)
    
    def assign_jobs_naive(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        #self.workers = []
        self.response = []
        q = Queue.PriorityQueue()
        for i in range(self.num_workers):
            q.put([0, i])
        for i in range(len(self.jobs)):
            worker = q.get()
            print worker[1], worker[0]
            q.put([worker[0]+self.jobs[i], worker[1]])
            
    def solve(self):
        self.read_data()
        self.assign_jobs()

job_queue = JobQueue()
job_queue.solve()