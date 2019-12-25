class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        res = []
        if nums is None or len(nums) <= 0:
            return res
        d = {0: -1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in d:
                res.append(i)
                res.append(d[sum] + 1)
                return res
            d[sum] = i
        return res


"""出现相同的sum则代表中间的子数组和为0"""
