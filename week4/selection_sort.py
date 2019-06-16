
def s_sort(arr):

    for idx, el in enumerate(arr):
        min = idx
        for i in range(idx +1, len(arr)) :
            if arr[i] < arr[min]: min = i 

        arr[idx] = arr[min]
        arr[min] = el

    return arr


test = [5, 5, 2, 6, 3]
print(s_sort(test))
