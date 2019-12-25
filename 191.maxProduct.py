class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        if not nums:
            return None

        res = nums[0]
        currentMax = currentMin = nums[0]
        for i in range(1, len(nums)):
            tempMax = currentMax
            currentMax = max(nums[i], currentMax * nums[i], currentMin * nums[i])
            currentMin = min(nums[i], currentMin * nums[i], tempMax * nums[i])
            res = max(res, currentMax)
        return res
s = Solution()
print(s.maxProduct([1, 2, 3, 4]))