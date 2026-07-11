def reverse_array(arr):
    arr.reverse()
    return arr

arr=list(map(int, input("Enter the elements: ").split()))
print("reversed array: ", reverse_array(arr))