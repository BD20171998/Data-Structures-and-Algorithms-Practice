'''
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
'''

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ""
        self.isWord = False
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self

        for w in word:

            if w not in node.children:
                node.children[w] = Trie()
                node.children[w].val = w

            node = node.children[w]

        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self

        for w in word:
            if w not in node.children:
                return False

            node = node.children[w]

        if node.isWord == True:
            return True

        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        def dfs(node):
            if node.isWord is True:
                return True

            for child in node.children.values():
                if dfs(child):
                    return True

            return False

        node = self

        for w in prefix:
            if w not in node.children:
                return False

            node = node.children[w]

        if node.isWord == True:
            return True

        else:
            return dfs(node)
