def Sec_largest(arr):
    arr.sort()
    secondlargest=arr[-2]
    
    return secondlargest    

arr = list(map(int, input("Enter the elements:").split()))
print("Second Largest element is :", Sec_largest(arr))
