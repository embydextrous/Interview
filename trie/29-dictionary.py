from trie import charToIndex

class DictionaryEntry:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"The meaning of {self.word} is '{self.meaning}'"

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.data = None

class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, meaning):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.data = DictionaryEntry(word, meaning)

    def searchMeaning(self, word):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                return "Not in Dictionary"
            p = p.children[index]
        return p.data.meaning

d = Dictionary()
d.insert("map", "a data structure to store key value pair")
d.insert("god", "human imagination for fighting")
d.insert("death", "end of life")
d.insert("birth", "beginning of life")
d.insert("computer", "a machine that can compute")
d.insert("modi", "tax ka bhooka fakir")
d.insert("sitaraman", "bartan maanjne wali aurat")

print(d.searchMeaning("yogi"))
print(d.searchMeaning("modi"))
print(d.searchMeaning("map"))


            
            

