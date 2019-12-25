class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[start] <= nums[mid]:
                if nums[mid] <= nums[end]:
                    end -= 1
                else:
                    start = mid
            else:
                if nums[mid] <= nums[end]:
                    end = mid
        if nums[start] <= nums[end]:
            return nums[start]
        else:
            return nums[end]


s = Solution()
a = [1, 2, 1]
print(s.findMin(a))