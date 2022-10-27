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

