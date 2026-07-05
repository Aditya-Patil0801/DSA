#Find Smallest Num in Array

arr=list(map(int, input("Enter the numbers:").split()))
print(arr)
arr.sort()
print(f"Smallest Number is {arr[0]}.")