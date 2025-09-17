# Merge Sort

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_array = arr[:mid]
    right_array = arr[mid:]

    Sorted_right = Merge_Sort(right_array)
    Sorted_left = Merge_Sort(left_array)

    return Merge(Sorted_left, Sorted_right)

def Merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


unsorted_array = [100, 25, 5, 77, 1, 6, 7, 99]
sorted_array = Merge_Sort(unsorted_array)
print("Sorted array is:",sorted_array)