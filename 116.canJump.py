class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        ans = 0
        for i in range(len(A) - 1):
            ans = max(ans, i + A[i])
            if ans < i:
                return False
        if ans >= len(A) - 1:
            return True
        return False
