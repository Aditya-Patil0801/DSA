#Find 2nd Largest element 


#METHOD-1
arr=list(map(int, input("Enter the Elements:").split()))
print(arr)
arr.sort()
print(f"{arr[-2]} is the second Largest element in an array.")


#METHOD-2
arr1=list(map(int, input("Enter the Elements:").split()))
print(arr1)
arr1.sort(reverse=True) #REVERSE-SORT
print(f"{arr1[1]} is the second Largest element in an array.")
