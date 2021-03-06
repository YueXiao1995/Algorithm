"""
给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。

示例:
    给定如下二叉树，以及目标和 sum = 22，

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    返回:

    3
    解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]

提示：
    节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paths-with-sum-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree import build

def pathSum(root, sum):
    def dfs(root, sum,  ancestors):
        if root == None:
            return 0
        paths = 0
        v = root.value
        if v == sum:
            paths += 1
            print([root.value])
        for i in range(len(ancestors)):
            v += ancestors[-i - 1]
            if v == sum:
                paths += 1
                print(ancestors[-i - 1:] + [root.value])
        ancestors.append(root.value)
        if root.left:
            paths += dfs(root.left, sum, list(ancestors))
        if root.right:
            paths += dfs(root.right, sum, list(ancestors))
        return paths

    return dfs(root, sum, [])

tree = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
print(tree)
sum = 22
print(pathSum(tree, sum))
