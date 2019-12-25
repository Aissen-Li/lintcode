class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        res = A[0]
        for i in range(1, len(A)):
            res ^= A[i]
        return res


s = Solution()
A = [2, 1, 1, 3, 3]
print(s.singleNumber(A))