import sys

def get_input_test_case1():

    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return input


def shiftdown(heap):
    c = len(heap) - 1
    p = (c - 1) >> 1
    while c > 0 and heap[c] < heap[p]:
        temp = heap[c]
        heap[c] = heap[p]
        heap[p] = temp
        c = p
        p = (c - 1) >> 1


def shiftup(heap):
    p = 0
    while 2 * p + 1 < len(heap):
        c = 2 * p + 1
        if c + 1 < len(heap) and heap[c] > heap[c + 1]:
            c += 1

        if heap[p] > heap[c]:
            temp = heap[p]
            heap[p] = heap[c]
            heap[c] = temp
            p = c
        else:
            break
up = []
down = []
n = get_input_test_case1()

for a_t in n:
    a_t = int(a_t)

    if not up:
        up.append(a_t)

    elif a_t > up[0]:
        up.append(a_t)
        shiftdown(up)

    else:
        down.append(-a_t)
        shiftdown(down)

    if len(up) < len(down):
        up.extend([-down[0]])
        shiftdown(up)
        down[0] = down[-1]
        down.pop()
        shiftup(down)
    elif len(up) > len(down) + 1:
        down.extend([-up[0]])
        shiftdown(down)
        up[0] = up[-1]
        up.pop()
        shiftup(up)

    if (len(up) + len(down)) % 2 == 0:
        result = float(up[0] - down[0]) / 2
        print('%.1f' % result)
    else:
        print('%.1f' % up[0])
