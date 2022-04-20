from trie import Trie, indexToChar

def printContents(root, chars):
    if root.isEndOfWord:
        print("".join(chars))
    for i in range(len(root.children)):
        if root.children[i] is not None:
            chars.append(indexToChar(i))
            printContents(root.children[i], chars)
            chars.pop()

trie = Trie(26)
words = ["vasu", "arpit", "sachi", "arjit", "atulya", "tumul", "punchun", "mickey", "archit", "chhotu", "haily", "arshit"]
for word in words:
    trie.insert(word)
printContents(trie.root, [])