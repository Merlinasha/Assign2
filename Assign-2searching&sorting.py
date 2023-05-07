#Implement Binary Search

def binary_search(arr, a, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == a:
            return mid
        elif array[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
a = 4
print("The given array is", arr)


#Implement Merge Sort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
    
        mergeSort(sub_array1)
        mergeSort(sub_array2)
     
        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
 
arr = [10, 9, 2, 4, 6, 13]
mergeSort(arr)
print(arr)

#Implement Quick Sort

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1 
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition (array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
  
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)

#Implement Insertion Sort

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
             
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


#Write a program to sort list of strings (similar to that of dictionary)

myDict = {'A': 10, 'B': 9,'C': 15, 'D': 2, 'E': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)



