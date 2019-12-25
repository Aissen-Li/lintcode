class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        if matrix == [[]]:
            return 0
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        col = 0
        count = 0

        while m != 0 and col != n:
            if matrix[m][col] == target:
                count += 1
                m -= 1
                col += 1
            elif matrix[m][col] > target:
                m -= 1
            else:
                col += 1

        if matrix[m][col] == target:
            count += 1
        else:
            if m == 0:
                A = [i for i in matrix[0][col+1:]]
                count += self.BinarySearch(A, target)
            if col == n:
                A = [i[-1] for i in matrix[:m]]
                count += self.BinarySearch(A, target)
        return count

    def BinarySearch(self, A, target):
        if not A: return 0
        if A[0] > target: return 0
        if A[-1] < target: return 0

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return 1
            elif A[mid] > target:
                end = mid
            else:
                start = mid
        if A[start] == target:
            return 1
        elif A[end] == target:
            return 1
        else:
            return 0