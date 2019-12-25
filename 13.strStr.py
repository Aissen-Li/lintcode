class Solution1:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        if target == '':
            return 0
        if source == '':
            return -1
        if len(target) > len(source):
            return -1
        for i in range(len(source)):
            if source[i] == target[0]:
                flag = True
                for j in range(1, len(target)):
                    if i + j >= len(source):
                        return -1
                    if source[i + j] == target[j]:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    print(i)
                    return i
        return -1


class Solution2:
    def strStr(self, source, target):
        return source.find(target)


"""KMP"""


class Solution3:
    def strStr(self, source, target):
        """生成针对source中各位置i的下一检查位置表，用于KMP"""
        i, k, m = 0, -1, len(target)
        target_next = [-1] * m
        while i < m-1:
            if k == -1 or target[i] == target[k]:
                i, k = i+1, k+1
                target_next[i] = k
            else:
                k = target_next[k]

        """主函数"""
        i, j = 0, 0
        n, m = len(source), len(target)
        while j < n and i < m:
            if i == -1 or source[j] == target[i]:
                j, i = j + 1, i + 1
            else:
                i = target_next[i]
        if i == m:
            return j-i
        return -1
