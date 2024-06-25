import time
def staircase_bottom_up(paths):
    # Making sure the base cases are covered
    if paths <= 0:
        return 1
    if paths <= 1:
        return 2

    # Create a list to store the number of ways to reach each step
    ways = [0] * (paths + 1)

    # Base cases
    ways[0] = 1
    ways[1] = 2
    if ways[paths -1] == 0:
        ways[paths -1] = staircase_bottom_up(paths -1)
    if ways[paths -2] == 0:
        ways[paths -2] = staircase_bottom_up(paths -2)
    return ways[paths-1] + ways[paths-2]

if __name__ == "__main__":
    paths = int(input("Enter the number of steps:"))
    start_time = time.time()
    ways = staircase_bottom_up(paths-1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The number of distinct ways to reach the top of the staircase with {paths} steps is: {ways}")
    print(f"Execution time: {execution_time} seconds")