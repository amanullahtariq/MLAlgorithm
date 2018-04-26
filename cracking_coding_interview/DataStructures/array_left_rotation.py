# Sample input
# 5 4
# 1 2 3 4 5

# Sample Output
# 5 1 2 3 4




def array_left_rotation(a,n,k):
    return (a[k:] + a[0:k])


def array_right_rotation(a,n,k):
    return (a[k-1:] + a[0:k-1])

a =[1, 2, 3, 4, 5]
k = 4
n = 5


print ' '.join(map(str,array_left_rotation(a,n,k)))


