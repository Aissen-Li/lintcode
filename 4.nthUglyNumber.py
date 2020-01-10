class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        pos = [0, 0, 0]
        res = [1]
        count = 1
        while count != n:
            minValue = min(res[pos[0]]*2, res[pos[1]]*3, res[pos[2]]*5)
            if minValue == res[pos[0]]*2:
                pos[0] += 1
            if minValue == res[pos[1]]*3:
                pos[1] += 1
            if minValue == res[pos[2]]*5:
                pos[2] += 1
            res.append(minValue)
            count += 1
        return res[-1]

s = Solution()
print(s.nthUglyNumber(9))
