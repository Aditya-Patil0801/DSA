# Rearrange array in increasing-decreasing order

def order_array(arr):
    arr.sort()
    n=len(arr)
    
    #reverse the 2nd half
    arr[n//2:]= reversed(arr[n//2:])
    return arr


arr= list(map(int, input("enter the elements: ").split()))
print("Increasing & Decreasing order is : ", order_array(arr))    