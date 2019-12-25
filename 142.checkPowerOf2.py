class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n < 0:
            return False
        n = bin(n)
        if n.count('1') == 1:
            return True
        else:
            return False

