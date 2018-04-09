class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.count = 0



class Trie:
    def __init__(self):
        self.root = self.getNode()

    def _charToIndex(self, char):
        return  ord(char) - ord('a')

    def getNode(self):
        return  TrieNode()

    def insert(self,key):
        current_trie = self.root
        length = len(key)

        for i in range(length):
            index = self._charToIndex(key[i])

            if not current_trie.children[index]:
                current_trie.children[index] = self.getNode()

            current_trie = current_trie.children[index]
            current_trie.count += 1

        current_trie.isEndOfWord = True

    def search(self,key):
        current_trie = self.root
        length = len(key)


        for i in range(length):
            index = self._charToIndex(key[i])
            #print(index)
            if not current_trie.children[index]:
                return None

            current_trie = current_trie.children[index]

        return  current_trie

    def count(self,key):
        count = 0
        current_trie = self.search(key)

        if current_trie:
            count = current_trie.count

        return count


file = open("input/trie_contacts.txt","r")
input = file.read().split()

n = int(input[0])
t = Trie()

for i in range(1, len(input),2):
    op = input[i]
    contact = input[i+1]

    if op == 'add':
        t.insert(contact)
    if op == 'find':
        print(t.count(contact))