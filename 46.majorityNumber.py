class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        value = nums[0]
        count = 0
        for i in nums:
            if value == i:
                count += 1
            else:
                count -= 1
            if count <= 0:
                value = i
        return value


s = Solution()
nums = [1, 2, 2, 3, 3]
print(s.majorityNumber(nums))