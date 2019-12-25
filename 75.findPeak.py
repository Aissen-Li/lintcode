class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if A[1] > A[2]:
            return 1
        if A[len(A) - 2] > A[len(A) - 3]:
            return len(A) - 2

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            if A[mid] < A[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1

        return start if A[start] >= A[end] else end
