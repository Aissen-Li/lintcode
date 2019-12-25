class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        res = 0
        record = [0] * 32
        for i in A:
            for j in range(-1, -32, -1):
                t = i & 1
                record[j] += t
                record[j] %= 3
                i >>= 1

        for i in range(32):
            res += record[31 - i] * pow(2, i)

        return res
