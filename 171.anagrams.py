class Solution1:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        temp = []
        result = []
        for i in range(len(strs)):
            s = list(strs[i])
            s.sort()
            t = ''.join(s)
            temp.append(t)
        for j in range(len(strs)):
            if temp.count(temp[j]) >= 2:
                result.append(strs[j])
        return result


"""自己写的算法，很菜，503ms，应该用hashmap解决"""


class Solution2:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        hashmap = {}
        result = []
        for items in strs:
            sort_item = ''.join(sorted(items))
            if sort_item in hashmap:
                hashmap[sort_item].append(items)
            else:
                hashmap[sort_item] = [items]
        for key in hashmap:
            if len(hashmap[key]) >= 2:
                result += hashmap[key]
        return result


"""用hash表某个[key]的元素长度来判断，因为存入的时候形式就是list，101ms"""
