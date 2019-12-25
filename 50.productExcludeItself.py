class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        left = [0]*len(nums)
        right = [0]*len(nums)
        B = [0]*len(nums)
        right[len(nums) - 1] = nums[-1]
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]
        # print(left)
        # print(right)
        B[0] = right[1]
        B[len(nums)-1] = left[-2]
        for i in range(1, len(nums) - 1):
            B[i] = left[i-1] * right[i + 1]
        return B


"""按照提示写出来的方法，多少有点dp的感觉，速度尚可，前缀积和后缀积分开处理"""
