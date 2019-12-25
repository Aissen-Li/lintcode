class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        res = []
        nums = sorted(nums)
        visited = [0 for _ in range(len(nums))]
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, subset, res, visited):
        if len(nums) == len(subset):
            res.append(subset[:])
        for i in range(len(nums)):
            if visited[i] == 1:
                continue
            if i >= 1 and visited[i-1] == 1 and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            visited[i] = 1
            self.dfs(nums, subset, res, visited)
            visited[i] = 0
            subset.pop()