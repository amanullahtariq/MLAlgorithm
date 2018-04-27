def solution(A):
    num = 1
    hash = set()

    for i in A:
        hash.add(i)

    while hash.__contains__(num):
        num +=1
    return  num

if __name__ == "__main__":
    A = [1, 3, 6, 4, 1, 2]

    print(solution(A))