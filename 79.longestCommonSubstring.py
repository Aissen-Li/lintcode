class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                longest_sub = 0
                flag = True
                while flag:
                    if i + longest_sub < len(A) and j + longest_sub < len(B):
                        if A[i + longest_sub] == B[j + longest_sub]:
                            longest_sub += 1
                        else:
                            flag = False
                    else:
                        flag = False
                ans = max(ans, longest_sub)
        return ans
"""252ms，有101ms的方法暂时还没有找到"""

