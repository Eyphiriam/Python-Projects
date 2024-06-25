def merge(A, left, mid, right):
    inversions = 0
    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            inversions += mid - i + 1
            temp.append(A[j])
            j += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= right:
        temp.append(A[j])
        j += 1

    for i in range(left, right + 1):
        A[i] = temp[i - left]

    return inversions

def merge_sort_and_count_inversions(A, left, right):
    if left < right:
        mid = (left + right) // 2
        left_inversions = merge_sort_and_count_inversions(A, left, mid)
        right_inversions = merge_sort_and_count_inversions(A, mid + 1, right)
        merge_inversions = merge(A, left, mid, right)
        return left_inversions + right_inversions + merge_inversions
    else:
        return 0

with open("Counting_Inversions_input.txt", "r") as input_file:
    for line in input_file:
        # Read the input from array
        array = [int(x) for x in line.strip().split(",")]

        # Print out the array
        print("Array:", array)

        # Count inversions using merge sort
        inversions = merge_sort_and_count_inversions(array, 0, len(array) - 1)

        # Print the number of inversions
        print("Number of inversions:", inversions)