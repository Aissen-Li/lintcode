class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        result = []
        num.sort()
        self.dfs(result, [], 0, num, target)
        return result

    def dfs(self, result, path, index, num, target):
        if target == 0:
            result.append(path[:])
            return
        for i in range(index, len(num)):
            if num[i] > target:
                break
            if i != index and num[i] == num[i-1]:
                continue
            path.append(num[i])
            self.dfs(result, path, i+1, num, target-num[i])
            path.pop()


test = Solution()
print(test.combinationSum2([7,1,2,5,1,6,10], 8))