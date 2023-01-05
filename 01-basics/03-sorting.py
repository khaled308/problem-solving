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


# selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


# insertion sort
def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# merge sort
def merge_sort(arr, start, end):
    if start >= end:
        return

    median = start + int((end - start) / 2)

    merge_sort(arr, start, median)
    merge_sort(arr, median + 1, end)
    merge(arr, start, end, median)


def merge(arr, start, end, sep):
    lst1 = []
    lst2 = []
    i = j = 0
    n1 = sep - start + 1
    n2 = end - sep

    while i < n1:
        lst1.append(arr[start + i])
        i += 1

    while j < n2:
        lst2.append(arr[sep + j + 1])
        j += 1

    i = j = 0
    k = start
    while i < n1 and j < n2:
        if lst1[i] <= lst2[j]:
            arr[k] = lst1[i]
            i += 1

        else:
            arr[k] = lst2[j]
            j += 1

        k += 1

    while i < n1:
        arr[k] = lst1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = lst2[j]
        j += 1
        k += 1


lst = [5, -7, 2, 10, 8, 3]
merge_sort(lst, 0, len(lst) - 1)
