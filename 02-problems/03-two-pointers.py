# find pair in sorted array which equal to target
def find_pair(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        pair_sum = lst[start] + lst[end]

        if pair_sum == target:
            return [lst[start], lst[end]]

        elif pair_sum < target:
            start += 1

        else:
            end -= 1

    return -1


# binary search
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        median = start + int((end - start) / 2)

        if lst[median] == target:
            return median

        elif lst[median] > target:
            end = median - 1

        else:
            start = median + 1

    return -1
