# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thr = list(range(n))  
    times = [0] * n
    
    for i in range(m):
    
        time = data[i]
        # find the smallest finish time
        thr_id = min(thr, key=lambda x: times[x])
        output.append((thr_id, times[thr_id]))  # assign to the thread
        times[thr_id] += time  # update the finish time

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    inp = input()
    n = int(inp.split()[0])
    m = int(inp.split()[1])

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
