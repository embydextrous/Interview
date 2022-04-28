from trie import Trie, indexToChar

def printContentsUtil(root, prefix):
    if root.isEndOfWord:
        print("".join(prefix))
    for i in range(len(root.children) - 1, -1, -1):
        if root.children[i] is not None:
            char = indexToChar(i)
            prefix.append(char)
            printContentsUtil(root.children[i], prefix)
            prefix.pop()

def printContents(root):
    if root is None:
        return
    for i in range(len(root.children) - 1, -1, -1):
        if root.children[i] is not None:
            char = indexToChar(i)
            printContentsUtil(root.children[i], [char])

names = ["sachi", "atulya", "prachi", "arshit", "soni", "tumul", "arpit", "haily", "mickey", "arjit", "chhotu", "archit", "vasu", "punchun"]
trie = Trie(26)
for name in names:
    trie.insert(name)

printContents(trie.root)
    