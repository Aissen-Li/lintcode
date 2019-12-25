class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        if a == b:
            return 0
        res = a ^ b
        count = 0
        if res > 0:
            while res != 0:
                res = res & (res - 1)
                count += 1
            return count
        if res < 0:
            res = abs(res - 1)
            while res != 0:
                res = res & (res - 1)
                count += 1
            return 32 - count


s = Solution()
print(s.bitSwapRequired(1, -1))