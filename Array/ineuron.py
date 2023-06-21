## Search for an element in an array and if the element is present in the array return its index.
# Linear search 
def element_search(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

array = [1,2,25,3,4,5,6,7]
output = element_search(array, 5)
print(f"{output}")


## Inserting an element in an array at a particular index.
# insert(index, element)

array.insert(2,5)
print(array)


## Removing an element from an array.
# remove(element)

array.remove(6)
print(array)



## counting the number of an element present in an array.
# count(element)

print(array.count(7))


## Deleting an element providing the index of the element
# arr.pop(index of element)

array.pop(3)
print(array)


## sorting an array
# arr.sort()

sorted_array = array.sort()
array = sorted_array
print(array)


## extending our array
# arr.extend([1,2,3])

array.extend([1,2,3])
print(array)
