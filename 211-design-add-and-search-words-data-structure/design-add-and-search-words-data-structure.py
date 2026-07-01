class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            if word[i] == '.':
                return any(dfs(i + 1, nxt) for c, nxt in node.items() if c != '#')
            return word[i] in node and dfs(i + 1, node[word[i]])
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)