class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        import sys
        n = len(nums)
        prefixMax, suffixMax = [0]*n, [0]*n
        prefixSum, suffixSum = [0]*n, [0]*n
        prefixMax[0] = prefixSum[0] = nums[0]
        suffixMax[-1] = suffixSum[-1] = nums[-1]

        for i in range(1, n):
            prefixSum[i] = max(prefixSum[i-1] + nums[i], nums[i])
            prefixMax[i] = max(prefixMax[i-1], prefixSum[i])
        for i in range(n-2, -1, -1):
            suffixSum[i] = max(suffixSum[i+1] + nums[i], nums[i])
            suffixMax[i] = max(suffixMax[i+1], suffixSum[i])
        res = -sys.maxsize
        for i in range(n-1):
            res = max(res, prefixMax[i] + suffixMax[i+1])
        return res