## reversing an array without using reverse or indexing .

def rev_arr(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1

    return arr



array = [1,2,3,4,5,6,7,8]
output = rev_arr(array)
print(f"Your reversed array is : {output}")




## Finding min and max in an array without using min max function

def find_min_max(arr):
    min = arr[0]
    max = arr[0]
    for element in arr:
        if element < min:
            min = element
        elif element > max:
            max = element

    return min , max

array = [-1,2,3,90,5,6,7,8,1]
output = find_min_max(array)
print(f"Your min and max element in the given array is : {output}")



## remove duplicates from an array without using any function

def dup_del(arr):
    unique_arr = []
    for elements in arr:
        if elements not in unique_arr:
            unique_arr.append(elements)

    return unique_arr
        

array = [1,2,3,3,21,4,5,4,7,8,5,8]
output = dup_del(array)
print(f"Your unique array without any duplicates values is : {output}")



## Returning the index of the first 8 from the given array using Binary Search 
array = [1,2,3,8,3,6,8,9,4,8]

def ret_index(arr , x):
    for i in range(0,len(arr)-1):
        if arr[i] == x :
            return i
    
    return -1

output = ret_index(array, 8) 
print(output)
