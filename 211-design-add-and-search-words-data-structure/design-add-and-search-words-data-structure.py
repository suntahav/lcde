class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node()
                node = node.children[c]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        def subsearch(node, word):
            if len(word) == 1:
                if word == '.':
                    for child in node.children.keys():
                        if node.children[child].isWord:
                            return True
                    return False
                elif word in node.children:
                    node = node.children[word]
                    return node.isWord
                else:
                    return False
            else:
                if word[0] == '.':
                    for child in node.children.keys():
                        res = subsearch(node.children[child], word[1:])
                        if res:
                            return True
                    return False
                else:
                    if word[0] not in node.children:
                        return False
                    else:
                        return subsearch(node.children[word[0]], word[1:])
        
        return subsearch(self.root, word)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)