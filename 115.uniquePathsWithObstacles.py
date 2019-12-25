class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        y = len(obstacleGrid)
        x = len(obstacleGrid[0])
        dp = [[0] * x for _ in range(y)]
        for i in range(x):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for j in range(y):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = 1
            else:
                break
        for j in range(1, y):
            for i in range(1, x):
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[-1][-1]
