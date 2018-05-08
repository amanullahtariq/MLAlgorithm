# Average Time Complexity:
# N Log (N)



class QuickSort():
    def __init__(self,arr):
        self.sorted_array = self.quicksort(arr, 0, len(arr) - 1)


    def swap(self,array, left, right):
        temp = array[left]
        array[left]  = array[right]
        array[right] = temp

        return array

    def partition(self,array, left, right, pivot):
        while left <= right:
            while array[left] < pivot:
                left +=1

            while array[right] > pivot:
                right -=1

            if left <= right:
                array = self.swap(array, left, right)
                left +=1
                right -=1

        return left


    def quicksort(self,arr, left_index, right_index):
        if left_index >= right_index:
            return

        pivot = arr[(left_index + right_index)/2]
        index = self.partition(arr, left_index, right_index, pivot)
        self.quicksort(arr, left_index, index - 1)
        self.quicksort(arr, index, right_index)

        return arr


A = [9, 2, 6, 4, 3, 5, 1]

print("Unsorted Array: ", A)

quicksort = QuickSort(A)

print("Unsorted Array: ", quicksort.sorted_array)