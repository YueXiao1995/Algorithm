"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
"""


def rotate(nums, k):
    new_nums = list(nums)
    l = len(nums)
    for i in range(0, l):
        nums[(i+k)%l] = new_nums[i]
    return nums

input = [1,2,3,4,5,6,7]

a = [1]
b = [2, 3]
print(rotate(input,0))
