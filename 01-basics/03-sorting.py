# Bubble sort
def bubbleSort(arr):
  for i in range(len(arr) - 1):
    swap = False
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swap = True
    
    if not swap:
      break

  return arr

# selection sort
def selectionSort(arr):
  for i in range(len(arr)):
    minimum = i
    for j in range(i + 1, len(arr)):
      if arr[minimum] > arr[j]:
        minimum = j
    
    arr[i], arr[minimum] = arr[minimum], arr[i]

  return arr

# insertion sort
def insertionSort(arr):
  for i in range(len(arr)):
    val = arr[i]
    j = i - 1
    while j >= 0 and val <  arr[j]:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = val
  return arr

# merge sort
def mergeSort(arr):
    if len(arr) <= 1:
      return arr

    mid = len(arr)//2
    arr1 = mergeSort(arr[:mid])
    arr2 = mergeSort(arr[mid:])
    return merge(arr1, arr2)

def merge(arr1, arr2):
  i = 0
  j = 0
  lst = []
  
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      lst.append(arr1[i])
      i += 1
    
    else:
      lst.append(arr2[j])
      j += 1
  
  while i < len(arr1):
    lst.append(arr1[i])
    i += 1
  
  while j < len(arr2):
    lst.append(arr2[j])
    j += 1

  return lst
