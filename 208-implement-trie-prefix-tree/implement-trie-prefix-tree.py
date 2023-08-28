class Trie:

    def __init__(self):
        self.trie = [0] * 27


    def insert(self, word: str) -> None:
        def _insert(trie, word):
            if type(trie[ord(word[0]) - ord('a') + 1]) == int:
                #No word like this so add new node

                #The new trie node
                trie[ord(word[0])- ord('a') + 1] = Trie()
                if len(word) == 1:
                    #forms a complete word
                    trie[ord(word[0])- ord('a') + 1].trie[0] = 1
                else:
                    #otherwise recursively add all the chars
                    _insert(trie[ord(word[0])- ord('a') + 1].trie, word[1:])
            else:
                if len(word) == 1:
                    trie[ord(word[0])- ord('a') + 1].trie[0] = 1
                else:
                    #the case the node is already a trie node or there has already been prefix like this
                    _insert(trie[ord(word[0])- ord('a') + 1].trie, word[1:])
        _insert(self.trie, word)
            
                

        

    def search(self, word: str) -> bool:
        # print(self.trie)
        temp_trie = self.trie
        for i in range(len(word)):
            if type(temp_trie[ord(word[i])- ord('a') + 1]) is not Trie:
                return False
            else:
                temp_trie = temp_trie[ord(word[i])- ord('a') + 1].trie
        if temp_trie[0] != 1:
            return False
        else:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        temp_trie = self.trie
        for i in range(len(prefix)):
            if type(temp_trie[ord(prefix[i])- ord('a') + 1]) is not Trie:
                return False
            else:
                temp_trie = temp_trie[ord(prefix[i])- ord('a') + 1].trie
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)