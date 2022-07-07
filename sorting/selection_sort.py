# Selection sort in Python


def selectionSort(arr, size):
   
    for i in range(size):
        min_idx = i

        for j in range(i+ 1, size):
         
   
            # select the minimum element in each loop
            if arr[j] < arr[min_idx]:
                min_idx = j
         
        # put min at the correct position
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])


data = [-3, 4, 99 ,31, -2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)