# Reverse an array.

def reverse (arr):
    return arr[: : -1]   # we can also do the same using reverse function

array = [1,2,3,4,5]
output = reverse(array)
print(f"My reversed array is : {output}")

# Find max and min element in an array.

def find_min_max(arr):
    return min(arr) , max(arr)

array = [1,2,3,4,5]
output = find_min_max(array)
print(f"Your minimum and maximum is : {output}")

# Find max and min element in an array without using min max function

def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]

    for elements in arr:
        if elements < minimum:
            minimum = elements
        if elements > maximum:
            maximum = elements
    return minimum , maximum

array = [1,2,3,4,5]
output = find_min_max(array)
print(f"Your minimum and maximum elements are : {output}")

## Remove duplicates from an array

def remove_dup(arr):
    return list(set(arr))

array = [1,2,3,4,1,25,6,2,3]
output = remove_dup(array)
print(f"Your array without duplicates values are : {output}")