class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        left = 0
        right = len(nums) - 1
        if left >= right:
            return 0
        pivot = k
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            while left < right and nums[left] < pivot:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if nums[left] < k:
            return left + 1
        else:
            return left


s= Solution()
num = [3, 2, 1]
k = 2
s.partitionArray(num, k)