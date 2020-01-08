class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        import sys
        n = len(nums)
        dp1 = [[-sys.maxsize for _ in range(k+1)] for _ in range(n+1)]
        dp2 = [[-sys.maxsize for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp1[i][0] = 0
            dp2[i][0] = 0
            for j in range(1, min(i+1, k+1)):  # 子数组数目不可能大于i与k的最小值
                dp1[i][j] = max(dp1[i-1][j] + nums[i-1],  # 并入第j组
                                dp1[i-1][j-1] + nums[i-1],  # 取了nums[i-2]，nums[i-1]自成第j组
                                dp2[i-1][j-1] + nums[i-1])  # 没有取nums[i-2], nums[i-1】自成第j组
                dp2[i][j] = max(dp1[i-1][j],  # 取nums[i-2]，前i-1个数分j组
                                dp2[i-1][j])  # 不取nums[i-2]
        return max(dp1[n][k], dp2[n][k])
