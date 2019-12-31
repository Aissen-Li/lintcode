class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        import sys
        n = len(A)
        dp = [[sys.maxsize] * 101 for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, 101):
                if i == 1:
                    dp[i][j] = abs(j - A[0])
                    continue
                for k in range(1, 101):
                    if abs(k-j) > target:
                        continue
                    else:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(j - A[i-1]))
        return min(dp[n])
