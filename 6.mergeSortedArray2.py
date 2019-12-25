class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        if A[0] >= B[-1]:
            return B+A
        if A[-1] <= B[0]:
            return A+B
        nums_sort = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                nums_sort.append(A[i])
                i += 1
            else:
                nums_sort.append(B[j])
                j += 1
        if i == len(A):
            nums_sort += B[j:]
        if j == len(B):
            nums_sort += A[i:]
        return nums_sort


s = Solution()
A = [1,2,3,4,5]
B = [5,6,7,8,9]
print(s.mergeSortedArray(A,B))