"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
     输入："aabcccccaaa"
     输出："a2b1c5a3"

示例2:
     输入："abbccd"
     输出："abbccd"
     解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。

提示：
    字符串长度在[0, 50000]范围内。
"""

def compressString(S):
    if len(S) == 0:
        return ""

    chars = [S[0]]
    freq = [1]
    for i in range(1, len(S)):
        if S[i] == chars[-1]:
            freq[-1] += 1
        else:
            chars.append(S[i])
            freq.append(1)

    if len(chars) * 2 >= len(S):
        return S

    compressed = ''
    for i in range(len(chars)):
        compressed += chars[i] + str(freq[i])
    return compressed

S = "aabcccccaaa"
print(compressString(S))


S = "abbccd"
print(compressString(S))
