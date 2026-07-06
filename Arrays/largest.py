#Find Largest Num in Array

#METHOD-1
arr=list(map(int, input("Enter the elements:").split()))
print(arr)
arr.sort()
print(f"{arr[-1]} is the largest element in an array.")


#METHOD-2
arr1=list(map(int, input("Enter the array elements:").split()))
print(arr1)
largest=arr1[0]
for i in range (len(arr1)):
    if arr1[i]>largest:
        largest=arr1[i]
        
print(f"{largest} is the largest element in an array.")


#METHOD-3
arr2=list(map(int ,input("Enter the elements :").split()))
print(arr2)
print(f"{max(arr2)} is the largest element in an array.")
