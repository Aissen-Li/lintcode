class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def preprocess(self, nums):

        pre_seg_max, pre_seg_min = [0], [0]
        presum_min, presum_max, presum = 0, 0, 0

        for num in nums:
            presum += num
            pre_seg_max.append(max(num, presum - presum_min))
            pre_seg_min.append(min(num, presum - presum_max))
            presum_min = min(presum_min, presum)
            presum_max = max(presum_max, presum)

        return pre_seg_max, pre_seg_min

    def maxDiffSubArrays(self, nums):
        import sys
        pre_seg_max, pre_seg_min = self.preprocess(nums)
        post_seg_max, post_seg_min = self.preprocess(nums[::-1])
        post_seg_max = post_seg_max[::-1]
        post_seg_min = post_seg_min[::-1]
        N = len(nums)
        res = -sys.maxsize
        for i in range(1, N):
            res = max(res, abs(pre_seg_max[i] - post_seg_min[i]))
            res = max(res, abs(pre_seg_min[i] - post_seg_max[i]))

        return res
