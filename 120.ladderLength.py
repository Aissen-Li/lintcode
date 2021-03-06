class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        from collections import deque
        dict.add(end)
        queue = deque([start])
        visited = set()
        visited.add(start)
        distance = 0
        while queue:
            distance += 1
            next_queue = deque()
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    visited.add(next_word)
                    next_queue.append(next_word)
            queue = next_queue
        return 0

    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for mid in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == mid:
                    continue
                words.append(left + mid + right)
        return words


test = Solution()
dic = set()
dic.add('a')
dic.add('b')
dic.add('c')
print(test.ladderLength('a', 'c', dic))