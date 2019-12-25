class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        if len(min(strs)) == 0:
            return ''
        k = len(strs)
        longest_prefix = 0
        flag = True
        while longest_prefix < len(strs[0]):
            for i in range(1, k):
                if strs[i][longest_prefix] != strs[0][longest_prefix]:
                    flag = False
            if not flag:
                break
            else:
                longest_prefix += 1
        return strs[0][0:longest_prefix]


"""101ms,思路没有理清，写了两遍才写对，双重循环"""


class Solution2:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        mins = min(strs)
        maxs = max(strs)
        pre = ""
        # now you can only work with maxs and mins
        for i in range(min(len(mins), len(maxs))):
            if mins[i] == maxs[i]:
                pre = pre + mins[i]
            else:
                break
        return pre


"""直接用最大值最小值来做，思路上更明确，101ms"""

