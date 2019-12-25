class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        s = 0
        for i in A:
            s ^= i
        last_one = s & (-s)
        res = [0, 0]
        for i in A:
            if i & last_one == 1:
                res[0] ^= i
            else:
                res[1] ^= i
        return res