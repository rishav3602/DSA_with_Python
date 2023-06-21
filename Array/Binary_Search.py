## Binary Search with recursion

def BinarySearch(arr,i,j,x):
    while i<=j:
        mid = i + (j-i)//2 
        if arr[mid] == x:
            return mid
        elif arr[mid] < x :
            return BinarySearch(arr,mid+1,j,x)
        else :
            return BinarySearch(arr,i,mid-1,x)
        
    return -1


array = [12, 15 ,17, 19, 23, 35, 39, 50]
x = 23
i = 0
j = len(array) - 1
output = BinarySearch(array,i,j,x)
# print(f"Your element is at index : {output}")


## Binary Search without recursion

def BinarySearch(arr,i,j,x):
    while i<=j:
        mid = i + (j-i)//2 
        if arr[mid] == x:
            return mid
        elif arr[mid] < x :
            i = mid+1
        else :
            j = mid-1 
            
    return -1


array = [12, 15 ,17, 19, 23, 35, 39, 50]
x = 17
i = 0
j = len(array) - 1
output = BinarySearch(array,i,j,x)
print(f"Your element is at index : {output}")