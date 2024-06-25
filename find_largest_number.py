def find_largest_number(arr):
    left, right = 0, len(arr) - 1
    max_num = -999  # Initialize max_num to a huge negative number for comparison

    while left < right - 1:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid
        else:
            right = mid

    # Find the max number without a built in function
    if arr[left] > max_num:
        max_num = arr[left]
    if arr[right] > max_num:
        max_num = arr[right]

    return max_num

def main():
    with open('find_largest_number_input.txt', 'r') as file:
        for line in file:
            nums = list(map(int, line.strip().split(',')))
            print(f"Array: {', '.join(map(str, nums))}")
            print(f"Max: {find_largest_number(nums)}")

if __name__ == "__main__":
    main()