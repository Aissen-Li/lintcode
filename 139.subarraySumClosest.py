class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        if not nums:
            return 0

        lst = [(0, 0)]
        for i in range(len(nums)):
            lst.append((lst[-1][0] + nums[i], lst[-1][1] + 1))
        lst.sort()

        min_diff = float('inf')
        ans = []
        for i in range(1, len(lst)):
            diff = lst[i][0] - lst[i-1][0]
            if diff < min_diff:
                start, end = lst[i-1][1], lst[i][1]

                if start > end:
                    start, end = end, start

                ans = [start, end - 1]
                min_diff = diff

        return ans

        return lst


s = Solution()
n = [1, 2, -2, 5]
print(s.subarraySumClosest(n))