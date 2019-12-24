class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # 万一有一个是空的，则最小长度就是逐个改变
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        # 开始递归，dp中dp[i][j]的定义是把长度位i的word1转到长度为j的word2所需要的最少步骤
        for i in range(m+1):
            for j in range(n+1):
                # 如果二者的当前位是相同的
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]


s = Solution()
print((s.minDistance('horse', 'ros')))