def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n) time
    """

    if len(list) <= 1: # stopping condition
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list)//2  # floor division
    left = list[:mid]
    right = list[mid:]

    return left, right  # return two values at the same time

def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
