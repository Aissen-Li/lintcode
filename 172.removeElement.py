class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        res = []
        for i in range(len(A)):
            if A[i] != elem:
                res.append(A[i])
        A[:len(res)] = res[:]
        return len(res)



s = Solution()
A = [3, 2, 1]
elem = 2
print(s.removeElement(A, elem))