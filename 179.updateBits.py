class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        # write your code here
        n &= 0xFFFFFFFF
        for k in range(j - i + 1):
            n &= ~(1 << k + i)

        n |= (m << i) & 0xFFFFFFFF

        if n & (1 << 31):
            n = -((~n + 1) & 0xFFFFFFFF)
        return n


