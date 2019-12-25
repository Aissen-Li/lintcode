class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        if not nums:
            return 0
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num] * k > len(nums):
                return num