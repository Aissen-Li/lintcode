class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if matrix[0][0] <= target <= matrix[-1][-1]:
            m = 0
            for i in range(len(matrix)):
                if matrix[i][0] <= target <= matrix[i][-1]:
                    m = i
                    break
        else:
            return False

        if target == matrix[m][0]:
            return True
        if target == matrix[m][-1]:
            return True

        begin = 0
        end = len(matrix[m]) - 1
        while True:
            mid = int((begin + end) / 2)
            if matrix[m][mid] == target:
                return True
            if matrix[m][mid] > target:
                begin = begin
                end = mid
            if matrix[m][mid] < target:
                begin = mid
                end = end
            if mid == int((begin + end) / 2):
                return False


s = Solution()
m =[[1,4,5],[6,7,8]]
t = 6
if s.searchMatrix(m, t):
    print('yes')
else:
    print('no')