# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thr = list(range(n))  # create a list of thread ids
    times = [0] * n  # initialize the finish time of each thread to 0
    for i in range(m):
        time = data[i]
        # find the thread with the smallest finish time
        thr_id = min(thr, key=lambda x: times[x])
        output.append((thr_id, times[thr_id]))  # assign the job to the thread
        times[thr_id] += time  # update the finish time of the thread
    """
        min_thr_id = thr[0]
        for j in range(1, n):
            if times[thr[j]] < times[min_thr_id]:
                min_thr_id = thr[j]
        output.append((min_thr_id, times[min_thr_id]))  # assign the job to the thread
        times[min_thr_id] += time  # update the finish time of the thread
        thr.remove(min_thr_id)  # remove the thread from the list of available threads
        thr.append(min_thr_id)
        """
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    inp = input()
    n = inp.split()[0]
    m = inp.split()[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))
    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_id, start_time in result:
        print(thread_id, start_time)


if __name__ == "__main__":
    main()
