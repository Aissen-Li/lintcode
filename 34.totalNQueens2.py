class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        if n <= 0:
            return 0
        res = []
        self.dfs(n, [], res)
        return len(res)

    def dfs(self, n, subSet, res):
        if len(subSet) == n:
            res.append(subSet)
        for column in range(n):
            if not self.check(subSet, column):
                continue
            subSet.append(column)
            self.dfs(n, subSet, res)
            subSet.pop()

    def check(self, subSet, column):
        currentRow = len(subSet)
        for dx in range(currentRow):
            if subSet[dx] == column or abs(subSet[dx] - column) == abs(dx - currentRow):
                # 这里后半部分比较其实就是用已经确定可以放置的点和将要放置的点作比较，确保斜率的绝对值为1 或者 -1
                # abs(subSet[dx] - column) == abs(dx - currentRow)
                # abs(y1-y2) == abs(x1-x2), x1, y1 表示已经确定的点的横坐标和纵坐标，x2, y2表示将要确定的那个点的横坐标和纵坐标

                return False
        return True
