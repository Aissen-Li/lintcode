class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        lst_s = []
        lst_t = []
        for i in s:
            lst_s.append(i)
        for j in t:
            lst_t.append(j)
        lst_s.sort()
        lst_t.sort()
        if lst_s == lst_t:
            return True
        else:
            return False





