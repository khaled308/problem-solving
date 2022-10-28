# linear search unordered list

def linearSearch(arr, element):
  for i in range(len(arr)):
    if arr[i] == element:
      return i
  return -1

# linear search ordered list

def orderedListLinearSearch(arr, element):
  for i in range(len(arr)):
    if arr[i] == element:
      return i
    if arr[i] > element:
      break
  return -1

# binary search using loops

def binarySearch(arr, element):
  left = 0
  right = len(arr) - 1
  
  while right >= left :
    mid = round((right + left) / 2)
    
    if arr[mid] == element:
      return mid
    
    elif arr[mid] > element:
      right = mid - 1
    
    elif arr[mid] < element:
      left = mid + 1
  
  return -1

# binary search using recursion

def binarySearchRecursion(arr, element):
  def helper(left, right):
    mid = round((right + left) / 2)
  
    if arr[mid] == element:
      return mid

    if (left > right):
      return -1
    
    elif arr[mid] < element :
      return helper(mid + 1, right)
    
    elif arr[mid] > element:
      return helper(left, mid - 1)
  
  return helper(0, len(arr) - 1)

# find given element in sorted and rotated array

def pivot(arr, low, high):
  
  mid = (low + high) // 2

  if low > high :
    return - 1

  if mid < high and arr[mid] > arr[mid + 1]:
    return mid + 1
  
  if mid > low and arr[mid] < arr[mid - 1]:
    return mid
  
  if arr[mid] < arr[low]:
      return pivot(arr, low, mid - 1)
    
  
  return pivot(arr, mid + 1, high)

def rotatedSortedArraySearch(arr, element):
  mid = pivot(arr, 0, len(arr))
  left = mid if element >= arr[mid] and element < arr[-1] else 0
  right = mid if left == 0 else len(arr) - 1
  
  while right >= left :
    mid = round((right + left) / 2)
    
    if arr[mid] == element:
      return mid
    
    elif arr[mid] > element:
      right = mid - 1
    
    elif arr[mid] < element:
      left = mid + 1
  
  return -1
