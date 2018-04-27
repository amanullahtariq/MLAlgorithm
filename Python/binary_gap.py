# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def binary_gap(num):
    if num == 1:
        return 0

    binary_gaps = []
    gap = 0
    for i in num:
       # print(i)
        if i == "0":
            gap = gap + 1
            #print (gap)
        else:
            binary_gaps.append(gap)
            gap = 0
    #print(binary_gaps)
    return max(binary_gaps)


def solution(N):
    # write your code in Python 3.6
    b = ("{0:b}".format(N))
    return(binary_gap(b))

print(solution(1041))