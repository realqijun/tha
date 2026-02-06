def getSecondLargest(arr):
    if arr is None or len(arr) < 2:
        return None

    largest = arr[0]
    largest_i = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_i = i

    second_l = arr[0] if largest_i != 0 else arr[1]
    for i in range(len(arr)):
        if i != largest_i and arr[i] > second_l:
            second_l = arr[i]
    return second_l

print(getSecondLargest([2, 3, 4, 2, 3]))