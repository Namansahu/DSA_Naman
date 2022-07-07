# Insertion sort in Python
def insertion_Sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        arr[j + 1] = key
n=int(input())
data=[]
for i in range(0,n):
	data.append(int(input()))
insertion_Sort(data)
print('Sorted Array in Ascending Order:')
print(data)