"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

Note:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
"""

from binarytree import build

def isCousins(root, x, y):
    def dfs(root, x, y, d, d_list):
        temp_d_list = [None, None]
        if root.value == x:
            temp_d_list[0] = d
            return temp_d_list
        if root.value == y:
            temp_d_list[1] = d
            return temp_d_list
        if root.left:
            return_left_d_list = dfs(root.left, x, y, d + 1, d_list)
            if return_left_d_list == True:
                return True
            elif return_left_d_list == False:
                return False
            else:
                temp_d_list = return_left_d_list

        if root.right:
            return_right_d_list = dfs(root.right, x, y, d + 1, d_list)
            if return_right_d_list == True:
                return True
            elif return_right_d_list == False:
                return False
            else:
                for i in range(2):
                    if return_right_d_list[i] != None:
                        temp_d_list[i] = return_right_d_list[i]

        if temp_d_list[0] != None and temp_d_list[1] != None:
            if temp_d_list[0] == temp_d_list[1]:
                if temp_d_list[0] == d + 1:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return temp_d_list

    result = dfs(root, x, y, 0, [None, None])
    if result == True:
        return True
    else:
        return False


root1 = build([1,2,3,4])
x1 = 4
y1 = 3
print(root1)
print(isCousins(root1, x1, y1))

root2 = build([1,2,3,None,4,None,5])
x2 = 5
y2 = 4
print(root2)
print(isCousins(root2, x2, y2))

root3 = build([1, 2, 3, None, 4])
x3 = 2
y3 = 3
print(root3)
print(isCousins(root3, x3, y3))

root4 = build([1,2,None,3,4,None,None,5])
print(root4)
x4 = 2
y4 = 4
print(isCousins(root1, x4, y4))


