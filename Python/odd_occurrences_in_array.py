## Detected time complexity:
## O(N) or O(N*log(N))


def solution(A):
    A.sort()
    print(A)

    for i in range(0, len(A) - 1, 2):
        if A[i] != A[i + 1]:
            return A[i]

    return A[i + 2]


A = [0, 0 , 1, 1, 2,2, 3,3, 2,2,4]

print (solution(A))