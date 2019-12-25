class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        if not nums:
            return [[]]

        nums = sorted(nums)
        res = []
        self.dfs(nums, [], 0, res)
        return res

    def dfs(self, nums, subset, index, res):
        res.append(list(subset))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, i + 1, res)
            subset.pop()