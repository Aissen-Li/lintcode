class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def __init__(self):
        self.wordSet = set()
        self.res = []

    def wordSearchII(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    self.dfs(board, trie.root.children[board[i][j]], i, j, {(i, j)})
        return self.res

    def dfs(self, board, node, x, y, visited):
        if node.word and node.word not in self.wordSet:
            self.wordSet.add(node.word)
            self.res.append(node.word)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]) and (x+dx, y+dy) not in visited and board[x+dx][y+dy] in node.children:
                visited.add((x+dx, y+dy))
                self.dfs(board, node.children[board[x+dx][y+dy]], x+dx, y+dy, visited)
                visited.remove((x+dx, y+dy))

