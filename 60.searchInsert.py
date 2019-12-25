class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if not A:
            return 0
        begin = 0
        end = len(A) - 1
        if A[-1] < target:
            return len(A)
        if A[-1] == target:
            return len(A) - 1
        if A[0] > target:
            return 0
        if A[0] == target:
            return 0

        while True:
            mid = int((begin + end) / 2)
            print(mid)
            if A[mid] == target:
                return mid
            if A[mid] < target < A[mid + 1]:
                return mid + 1
            else:
                if A[mid] > target:
                    end = mid
                    begin = begin
                if A[mid] < target:
                    begin = mid
                    end = end


s = Solution()
a = [1, 2, 5, 7]
print(s.searchInsert(a, 1))