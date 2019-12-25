class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        index = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[index] == nums[i] and count < 2:
                count += 1
                index += 1
                nums[index] = nums[i]
            if nums[index] != nums[i]:
                index += 1
                count = 1
                nums[index] = nums[i]
        return index + 1


s = Solution()
n = [1,1,1,2,2,2]
print(s.removeDuplicates(n))