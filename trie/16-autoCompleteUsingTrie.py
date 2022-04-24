from trie import Trie, charToIndex, indexToChar

# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/

class AutoComplete:
    def __init__(self, words):
        self.trie = Trie(26)
        for word in words:
            self.trie.insert(word)

    def search(self, query):
        p = self.trie.root
        for c in query:
            index = charToIndex(c)
            if p.children[index] is None:
                return []
            p = p.children[index]
        result = []
        self.printAll(p, query, [], result)
        return result

    def printAll(self, root, query, suffix, result):
        if root.isEndOfWord:
            result.append(f'{query}{"".join(suffix)}')
        for i in range(len(root.children)):
            char = indexToChar(i)
            if root.children[i] is not None:
                suffix.append(char)
                self.printAll(root.children[i], query, suffix, result)
                suffix.pop()

words = ["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"]
autoComplete = AutoComplete(words)
print(autoComplete.search("he"))
