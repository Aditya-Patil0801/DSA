def median_arr(arr):
    arr.sort()
    n=len(arr)
    if n % 2 == 1:          # Odd number of elements
        median = arr[n // 2]
    else:                   # Even number of elements
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2

    return median
arr = list(map(int, input("Enter the elemnts: ").split()))
print("Median of the given array is: " ,median_arr(arr))