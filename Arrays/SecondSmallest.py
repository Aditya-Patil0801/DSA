def Sec_smallest(arr):
    arr.sort()
    secondsmallest=arr[1]
    
    return secondsmallest    

arr = list(map(int, input("Enter the elements:").split()))
print("Second Smallest element is :", Sec_smallest(arr))
