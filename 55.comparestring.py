class Solution1:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        A = list(A)
        B = list(B)
        for i in B:
            try:
                A.remove(i)
            except:
                return False
        return True


class Solution2:
    def compareStrings(self, A, B):
        # write your code here
        if len(A) < len(B):
            return False
        if len(A) == len(B):
            return(sorted(A) == sorted(B))
        for i in B:
            if A.count(i) < B.count(i):
                return False
        return True

"""自己写的是删除方法，另一种是判断长短的排序方法"""