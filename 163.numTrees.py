class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        A = [1, 1, 2]
        if n < 3:
            return A[n]
        for i in range(3, n + 1):
            res = 0
            for k in range(1, i+1):
                res += A[k - 1] * A[i - k]
            A.append(res)
        return A[-1]

