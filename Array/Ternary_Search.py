## Searching the element in an array by dividing the array into three parts.

def Ternary_Search(arr, x):
    left = 0
    right = len(arr)-1
    mid1 = left + (right-left)//3
    mid2 = right + (left-right)//3

    while left <= right :
        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif arr[mid1] > x:
            right = mid1 - 1
        elif arr[mid2] < x:
            left = mid2 + 1
        else :
            left = mid1 + 1
            right = mid2 - 1

    return -1

array = [1,2,3,4,5,6,7,8,9]
output = Ternary_Search(array, 5)
print(output) 
