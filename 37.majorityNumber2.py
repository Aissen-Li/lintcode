class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        if not nums:
            return 0
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num] * 3 > len(nums):
                return num