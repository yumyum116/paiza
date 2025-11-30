def selection_sort(array, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
    
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            