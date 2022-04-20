'''
Given a dictionary of words where each word follows CamelCase notation, print all words in the dictionary that
match with a given pattern consisting of uppercase characters only.
CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with
a capital letter. Common examples include: “PowerPoint” and “WikiPedia”, “GeeksForGeeks”, “CodeBlocks”, etc.
Examples: 
 

Input: 
dict[] = ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek", 
"HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "HT",
Output: ["HiTech", "HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "H",
Output: ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek", 
    "HiTechWorld", "HiTechCity", "HiTechLab"]

For pattern "HTC",
Output: ["HiTechCity"]


Input: 
dict[] = ["WelcomeGeek","WelcomeToGeeksForGeeks", "GeeksForGeeks"]

For pattern "WTG",
Output: ["WelcomeToGeeksForGeeks"]

For pattern "GFG",
Output: [GeeksForGeeks]

For pattern "GG",
Output: No match found
'''
def charToIndex(c):
    return ord(c) - ord('A')

def isCapitalLetter(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if isCapitalLetter(c):
                index = charToIndex(c)
                if p.children[index] is None:
                    p.children[index] = TrieNode()
                p.children[index].words.append(word)
                p = p.children[index]

    def search(self, pat):
        p = self.root
        for c in pat:
            index = charToIndex(c)
            if p.children[index] is None:
                return []
            p = p.children[index]
        return p.words

words = ["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek", "HiTechWorld", "HiTechCity", "HiTechLab"]
trie = Trie()
for word in words:
    trie.insert(word)
print(trie.search("H"))
print(trie.search("HT"))
print(trie.search("HG"))
print(trie.search("HTC"))
print(trie.search("HTCP"))


