class Node:
    def __init__(self):
        self.children = {}
        self.isEndWord = False
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                node.children[word[i]] = Node()
                node = node.children[word[i]]

            if i == len(word) - 1:
                node.isEndWord = True
        

        

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                return False
            else:
                node = node.children[word[i]]
        return node.isEndWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return False
            else:
                node = node.children[prefix[i]]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)