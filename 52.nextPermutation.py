class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        flag = 0
        change = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                change = i-1
                print(change)
                flag = 1
                break

        if not flag:
            nums.reverse()
            return nums

        for i in range(len(nums)-1, change, -1):
            if nums[i] > nums[change]:
                nums[i], nums[change] = nums[change], nums[i]
                break

        resort = nums[change + 1:]
        print(resort)
        resort.sort()
        print(resort)
        nums[change + 1:] = resort
        return nums


s = Solution()
print(s.nextPermutation([1, 2, 1]))
