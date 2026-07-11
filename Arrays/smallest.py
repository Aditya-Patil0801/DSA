#wap to print the smallest number in array.

def Smallest(arr):
    smallest=arr[0]
    
    for i in range(len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
        
    return smallest

arr=list(map(int, input("Enter the elements:").split()))
print("smallest element is ",Smallest(arr))