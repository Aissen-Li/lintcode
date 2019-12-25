class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if nums[-1] > nums[0]:
            return nums[0]
        else:
            start = 0
            end = len(nums) - 1
            while end-start > 1:
                mid = (start+end)//2
                if nums[mid] < nums[end]:
                    end = mid
                elif nums[mid] > nums[start]:
                    start = mid
            return min(nums[start], nums[end])