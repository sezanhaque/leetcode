from collections import defaultdict


class Trie:

    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        if not word:
            self.isWord = True
        else:
            self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.isWord
        if word[0] in self.children:
            return self.children[word[0]].search(word[1:])

        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])

        return False


obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))


