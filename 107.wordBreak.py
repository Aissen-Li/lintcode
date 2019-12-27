class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        maxLen = max(len(w) for w in dict)
        for i in range(1, n + 1):
            for j in range(1, min(i, maxLen) + 1):
                if not dp[i -j]:
                    continue
                else:
                    if s[i-j: i] in dict:
                        dp[i] = True
                        break
        return dp[n]

