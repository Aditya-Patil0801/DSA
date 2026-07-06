#Find Smallest Num in Array


#METHOD-1
arr=list(map(int, input("Enter the elements:").split()))
print(arr)
arr.sort()
print(f"Smallest element is {arr[0]}.")


#METHOD-2
arr1=list(map(int, input("Enter the elements:").split()))
print (arr1)
smallest=arr1[0]

for i in range(len(arr1)):
    if arr1[i]< smallest:
        smallest=arr1[i]
        
print(f"Smallest element is {smallest}.")

#method-3
arr2=list(map(int, input("Enter the elements:").split()))
print (arr2)
print(f"Smallest eleement is {min(arr2)}.")