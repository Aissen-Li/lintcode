class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        if not str:
            return 0
        str = str.strip()
        res = ''
        if str[0] == '-' or str[0] == '+':
            if str[1] != '-' and str[1] != '+':
                res += str[0]
                str = str[1:]
            else:
                return 0

        for i in str:
            if '0' <= i <= '9':
                res += i
            else:
                break
        if len(res) == 0:
            return 0
        if int(res) > 2147483647:
            return 2147483647
        if int(res) < -2147483648:
            return -2147483648
        return int(res)


"""101ms,没有太大意义，一点一点试出来"""