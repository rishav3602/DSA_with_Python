def arr_sort(arr):
    sorted_array = list()
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            sorted_array.append(i)
    print (sorted_array)

array = [1,4,3,8,2,9,10,6]
output = arr_sort(array)
print(output)
