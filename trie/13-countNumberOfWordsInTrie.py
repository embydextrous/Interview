from trie import Trie

def countWordsUtil(p, count):
    if p.isEndOfWord:
        count[0] += 1
    for i in range(len(p.children)):
        if p.children[i] is not None:
            countWordsUtil(p.children[i], count)

def countWords(trie):
    p = trie.root
    count = [0]
    countWordsUtil(p, count)
    return count[0]

words = ["vasu", "arpit", "sachi", "arjit", "atulya", "tumul", "punchun", "mickey", "archit", "chhotu", "haily", "arshit"]
trie = Trie(26)
for word in words:
    trie.insert(word)
print(countWords(trie))
