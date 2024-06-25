import time

def staircase_naive(paths):
    if paths == 0:
        return 1
    if paths == 1:
        return 2
    return staircase_naive(paths-1) + staircase_naive(paths-2)
                                                  
if __name__ == "__main__":
    paths = int(input("Enter the number of steps:"))
    start_time = time.time()
    ways = staircase_naive(paths-1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The number of distinct ways to reach the top of the staircase with {paths} steps is: {ways}")
    print(f"Execution time: {execution_time} seconds")


