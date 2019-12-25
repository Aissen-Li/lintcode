class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if not nums:
            return [[]]

        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, subset, res):
        if len(nums) == len(subset):
            res.append(subset[:])
        for i in range(len(nums)):
            if nums[i] not in subset:
                subset.append(nums[i])
                self.dfs(nums, subset, res)
                subset.pop()


test = Solution()
print(test.permute([1,2,3]))
