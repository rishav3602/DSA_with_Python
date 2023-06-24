## Sort the given array using insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key
    
    return arr

array = [12,3,56,34,23,89,20]
output = insertion_sort(array)
print(f"Your sorted array using insertion sort is : {output}")

