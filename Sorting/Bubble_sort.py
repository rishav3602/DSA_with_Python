## Sort the given array using bubble sort

def bubbleSort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

array = [70,20,50,30,90,5,15]
output = bubbleSort(array)
print(f"The sorted array using bubble sort is : {output}")