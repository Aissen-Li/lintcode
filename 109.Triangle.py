class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        n = len(triangle)
        # dp数组代表从（0,0）走到（i,j）所需要的最小数值
        dp = [[0] * (i+1) for i in range(n)]
        # 初始化dp数组，往下走只能走相邻的两个数字，不能遍历之后随便走
        # 初始位置就在第一个数，所以是0
        dp[0][0] = triangle[0][0]
        # 每一行的第一个数和最后一个数比较特殊，因为只有一条路可以走到
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[n-1])
#  滚动数组法类似于只保留两行内容作为空间，就要注意i变成i%2,i-1变成(i-1)%2
