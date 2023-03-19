from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root

        for char in word:
            root = root.children.setdefault(char, TrieNode())

        root.end = True

    def search(self, word: str) -> bool:
        def DFS(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                return node.end

            if word[idx] == ".":
                for child in node.children:
                    if DFS(node.children[child], idx + 1):
                        return True

            if word[idx] in node.children:
                return DFS(node.children[word[idx]], idx + 1)

        return DFS(self.root, 0)


obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))


class WordDictionary_Set:
    # Fast

    def __init__(self):
        self.dictionary = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.dictionary[len(word)]

        for el in self.dictionary[len(word)]:
            for idx, char in enumerate(word):
                if char != el[idx] and char != ".":
                    break
            else:
                return True

        return False


obj2 = WordDictionary_Set()
obj2.addWord("bad")
obj2.addWord("dad")
obj2.addWord("mad")
print(obj2.search("pad"))
print(obj2.search("bad"))
print(obj2.search(".ad"))
print(obj2.search("b.."))
