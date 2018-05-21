def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)


        # Merge two list here
        index = 0
        left_start = 0
        right_start = 0

        while left_start < len(left) and right_start < len(right):
            if left[left_start] < right[right_start]:
                alist[index] = left[left_start]
                left_start +=1
            else:
                alist[index] = right[right_start]
                right_start +=1
            index +=1

        while left_start < len(left):
            alist[index] = left[left_start]
            left_start +=1
            index +=1

        while right_start < len(right):
            alist[index] = right[right_start]
            right_start +=1
            index +=1




alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
