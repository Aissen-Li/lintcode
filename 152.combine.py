class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        self.result = []
        nums = []
        for i in range(n):
            nums.append(i + 1)

        self.dfs(nums, k, [], 0)

        return self.result

    def dfs(self, nums, k, subset, start_id):
        if len(subset) == k:
            self.result.append(subset)
            return
        for i in range(start_id, len(nums)):
            self.dfs(nums, k, subset + [nums[i]], i + 1)