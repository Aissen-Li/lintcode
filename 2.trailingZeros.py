class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        result = 0
        temp = n // 5
        while temp != 0:
            result += temp
            temp //= 5
        return result