# Merge Sort is O(nlogn) time complexity

def merge_sort(base_array):
    # If there's only 1 item in list, it is sorted
    array_size = len(base_array)
    if array_size < 2:
        return

    # Otherwise, split the list in half (divide & conquer)
    array_middle = array_size // 2
    left_side = base_array[0:array_middle]
    right_side = base_array[array_middle:]

    # Recursively, solve this problem
    merge_sort(left_side)
    merge_sort(right_side)

    # Now the list halves are merged to rebuild the base_array
    base_array.clear()
    while len(left_side) + len(right_side) > 0:
        if len(right_side) == 0 or (len(left_side) > 0 and left_side[0] < right_side[0]):
            base_array.append(left_side.pop(0))
        else:
            base_array.append(right_side.pop(0))
    return base_array


if __name__ == '__main__':

    my_array = [5, 20, 23, 55, 88, 109, 2, 4, 8, 5, 3, 1]

    print("This is the base array which is unsorted:")
    for i in my_array:
        print(i)

    sorted_array = merge_sort(my_array)

    print("\nThis is the sorted array:")
    for i in sorted_array:
        print(i)
