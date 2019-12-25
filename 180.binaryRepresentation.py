class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binaryRepresentation(self, n):
        if '.' not in n:
            return bin(int(n))[2:]
        integer, decimal = n.split('.')
        integer = int(integer)
        decimal = float('0.' + decimal)

        s1 = bin(integer)[2:]
        if decimal == 0:
            return s1
        s2 = ''
        count = 32
        while count > 0:
            count -= 1
            decimal *= 2
            if decimal >= 1:
                s2 += '1'
                decimal -= 1
                if decimal == 0:
                    return s1 + '.' + s2
            else:
                s2 += '0'
        return 'ERROR'


s = Solution()
print(s.binaryRepresentation('3.25'))