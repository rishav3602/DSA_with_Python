## Sort the given array using selection sort

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1 , n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

    return arr

array = [ 23,18,34,90,12,56,10,23]
output = selectionSort(array)
print(f"Your sorted array using selection sort is : {output}")
            