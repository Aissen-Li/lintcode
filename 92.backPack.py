class Solution1:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        n = len(A)
        res = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            res[i][0] = 0
        for i in range(1, n+1):
            res[0][i] = 0
        A = sorted(A)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i < A[j-1]:
                    pass
                else:
                    res[i][j] = max(res[i][j-1], res[i-A[j-1]][j-1] + A[j-1])
        return res[m][n]


class Solution2:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        A.sort()
        dp = [0] * (m+1)
        dp[0] = 1
        res = 0
        for size in A:
            start = res
            for i in range(start+1, m+1):
                if i-size >= 0 and dp[i-size]:
                    res = i
                    dp[i] = 1
                if res - start == size:
                    break
        return res