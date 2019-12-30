class Solution1:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if not s1 and not s2 and not s3:
            return True
        if not s1 and s2 != s3:
            return False
        if not s2 and s1 != s3:
            return False

        m = len(s1)
        n = len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = s1[:i] == s3[:i]
        for i in range(1, n+1):
            dp[0][i] = s2[:i] == s3[:i]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    if s2[j-1] == s3[i+j-1]:
                        dp[i][j] = dp[i][j-1]
        return dp[m][n]


class Solution2:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        if m == 0 or n == 0:
            return s1 == s3 or s2 == s3
        dp = [True] + [False for _ in range(n)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = dp[j] and s1[i-1] == s3[i+j-1] or dp[j-1] and s2[j-1] == s3[i+j-1]
        return  dp[n]