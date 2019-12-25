class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.dfs(result, [], 0, candidates, target)
        return result

    def dfs(self, result, path, index, candidates, target):
        if target == 0:
            result.append(path[:])
            return
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            path.append((candidates[i]))
            self.dfs(result, path, i, candidates, target - candidates[i])
            path.pop()
