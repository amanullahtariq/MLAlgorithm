def quicksort(arr):
    quicksort(arr, 0, len(arr) - 1)


def quicksort(arr, left_index, right_index):
    if left_index >= right_index:
        return

    pivot = arr[(left_index + right_index)/2]

