#### Create a tree such that maximum value is root
##         9
##       //  \\
##      3 4  5   6
##     //    /\ /\
##     0    0
###########################


import numpy as np

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def find_max(arr):
    index = 0
    max = 0
    for i in range(0,arr.__len__()):
        if max <= arr[i]:
            max = arr[i]
            index = i

    return  index,max

def create_node(arr, root):
    index, max_value = find_max(arr)

    if arr.__len__() == 0:
        return

    if root == None:
        root.data = max_value

    root.left = Tree()
    #Left Node
    create_node(arr[0:index], root.left )
    # Right Node
    root.right = Tree()
    create_node(arr[index+1:], root.right)

    #return  root

input = [3,4,0,9,5,6,1,0]
root = Tree()

create_node(input, root)
print(root.data)

