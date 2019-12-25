class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                return mid
            if A[start] < A[mid] < A[end]:
                if target > A[mid]:
                    start = mid
                    continue
                if target < A[mid]:
                    end = mid
                    continue
            if A[mid + 1] > A[mid] > A[mid - 1]:
                if A[start] <= target:
                    if target > A[mid]:
                        if A[mid] < A[end]:
                            end = mid
                            continue
                        if A[mid] > A[start]:
                            start = mid
                            continue
                    if target < A[mid]:
                        end = mid
                        continue
                if A[end] >= target:
                    if target > A[mid]:
                        start = mid
                        continue
                    if target < A[mid]:
                        if A[mid] > A[start]:
                            start = mid
                            continue
                        if A[mid] < A[end]:
                            end = mid
            if A[mid] < A[mid + 1] and A[mid] < A[mid - 1]:
                if target < A[mid]:
                    return -1
                if target > A[mid]:
                    if target >= A[start]:
                        end = mid - 1
                        continue
                    if target <= A[end]:
                        start = mid
                        continue
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                if target > A[mid]:
                    return -1
                if target < A[mid]:
                    if target >= A[start]:
                        end = mid
                        continue
                    if target <= A[end]:
                        start = mid + 1
                        print(start, end)
                        continue
        print(start, end)
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


s = Solution()
a = [6,8,9,1,3,5]
print(s.search(a, 5))