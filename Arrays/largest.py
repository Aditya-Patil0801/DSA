#Find Largest Num in Array

def Largest(arr):
    largest=arr[0]
    
    for i in range(len(arr)):
        if arr[i] > largest:
            largest=arr[i]
            
    return largest


arr=list(map(int, input("Enter the elements:").split()))
print("Largest element is ",Largest(arr))