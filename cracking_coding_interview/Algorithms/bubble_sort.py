def get_input():
    file = open('inputs/bubble_sort.txt')
    input = file.read()
    file.close()
    return  input

def bubble_sort(a, n):
    swap_count = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n-1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                is_sorted = False

    return a, swap_count

n, a = get_input().split('\n')

n = int(n)
a = list(map(int, a.split(' ')))

a, swap_count = bubble_sort(a, n)


print('Array is sorted in {} swaps.'.format(swap_count))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[n-1]))