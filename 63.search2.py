class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        if not A:
            return False
        if A[0] == target or A[-1] == target:
            return True
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return True
            if A[mid] > A[start]:
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] == A[start]:
                start += 1
            else:
                if A[mid] < target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target or A[end] == target:
            return True
        else:
            return False
