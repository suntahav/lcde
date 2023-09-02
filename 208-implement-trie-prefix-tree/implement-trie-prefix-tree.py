class Node:
    def __init__(self):
        self.children = {}
        self.isEndWord = False
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node()
                node = node.children[c]

        node.isEndWord = True
        

        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return node.isEndWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            else:
                node = node.children[c]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)