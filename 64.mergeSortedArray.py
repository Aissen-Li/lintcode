class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        if m == 0:
            A[:] = B[:]
        if n != 0:
            i, j = m - 1, n - 1
            pos = m + n - 1
            while True:
                if A[i] <= B[j]:
                    A[pos] = B[j]
                    j -= 1
                    if j == -1:
                        break
                else:
                    A[pos] = A[i]
                    i -= 1
                    if i == -1:
                        A[:j+1] = B[:j+1]
                        break
                pos -= 1
                if pos == -1:
                    break


s = Solution()
a = [3, 5, 0, 0, 0]
b = [1, 2, 4]
print(s.mergeSortedArray(a, 2, b, len(b)))
