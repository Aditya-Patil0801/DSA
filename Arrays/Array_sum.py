#calculating sum of the elements of the array

def total(arr):
    sum=0
    i=arr[0]
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum

arr = list(map(int,input("Enter the elements:").split()))
print("Sum of the elements of the array is: ",total(arr))
        