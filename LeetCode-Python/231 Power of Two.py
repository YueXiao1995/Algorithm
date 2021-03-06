"""
Given an integer, write a function to determine if it is a power of two.

Example 1:
    Input: 1
    Output: true
    Explanation: 20 = 1

Example 2:
    Input: 16
    Output: true
    Explanation: 24 = 16

Example 3:
    Input: 218
    Output: false
"""

def isPowerOfTwo(n):
    if n == 0:
        return False

    while n % 2 == 0:
        n //= 2

    if n == 1:
        return True
    else:
        return False

input1 = 1
input2 = 16
input3 = 218
print(isPowerOfTwo(0))
