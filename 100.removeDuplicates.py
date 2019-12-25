class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        pos = 1
        for point in range(len(nums)-1):
            if nums[point] != nums[point + 1]:
                nums[pos] = nums[point + 1]
                pos += 1
        return pos


"""自己写的办法比较慢1211ms"""
s = Solution()
a = []
print(s.removeDuplicates(a))


