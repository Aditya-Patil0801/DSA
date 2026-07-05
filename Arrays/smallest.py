#Find Smallest Num in Array


# #METHOD-1
# arr=list(map(int, input("Enter the numbers:").split()))
# print(arr)
# arr.sort()
# print(f"Smallest Number is {arr[0]}.")


# #METHOD-2
# arr=list(map(int, input("Enter the numbers:").split()))
# print (arr)
# smallest=arr[0]

# for i in range(len(arr)):
#     if arr[i]< smallest:
#         smallest=arr[i]
        
# print(f"Smallest Number is {smallest}.")

#method-3
arr=list(map(int, input("Enter the numbers:").split()))
print (arr)
print(f"Smallest number is {min(arr)}.")