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

## Binary search in 2d array

def Binary_Search_Matrix(arr,x):
    m = len(arr)
    if m == 0:
        return False
    n = len(arr[0])

    start = 0
    end = m*n-1

    while start <= end:
        mid = start + (end-start)//2
        mid_element = arr[mid//n][mid%n]
        if mid_element == x:
            return True
        elif mid_element < x:
            start = mid + 1
        else: 
            end = mid - 1
        
    return False

array = [[1,3,5,7],[10,13,16,20],[23,30,34,60]]
x = 33
output = Binary_Search_Matrix(array, x)
print(output)