class Solution1:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        if not nums:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            k = len(nums) - 1
            while True:
                if nums[k-1] == nums[k]:
                    k = k-1
                else:
                    return k

        begin = 0
        end = len(nums) - 1
        while True:
            mid = int((begin + end) / 2)
            if target > nums[mid]:
                begin = mid
                end = end
            if target < nums[mid]:
                end = mid
                begin = begin
            if target == nums[mid]:
                while True:
                    if nums[mid - 1] == nums[mid]:
                        mid = mid - 1
                    else:
                        return mid
            if mid == int((begin + end) / 2):
                return -1


s = Solution1()
n = [1, 2, 3, 6, 8, 9, 9, 9]
print(s.binarySearch(n, 1))


class Solution2:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
