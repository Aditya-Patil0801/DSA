#Reversing an array

arr=list(map(int, input("Enter the Elements:").split()))
print(arr)

#METHOD-1
arr.reverse()  
print(arr)


#METHOD2-
reversed_arr=arr[::-1]
print(reversed_arr)