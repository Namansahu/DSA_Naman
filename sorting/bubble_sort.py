# Bubble sort in Python

def bubble_Sort(arr):
    
  # loop to access each array element
  for i in range(len(arr)):
    # keep track of swapping
    swapped = False
    # loop to compare array elements
    for j in range(0, len(arr) - i - 1):

      # compare two adjacent elements in array 
      if arr[j] > arr[j + 1]:

        # swapping elements if elements
        arr[j],arr[j+1]=arr[j+1],arr[j]
	      swapped = True
    # no swapping means the array is already sorted
    if not swapped:
      break

data = [3,1,6,-8,3,2]

bubble_Sort(data)

print('Sorted Array in Ascending Order:')
print(data)