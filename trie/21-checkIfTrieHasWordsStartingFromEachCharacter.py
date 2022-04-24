'''
Given a Trie, the task is to check if it contains words starting from every alphabet from [a - z].

Examples:

    Input: keys[] = {"element", "fog", "great", "hi",
    "ok", "ios", "parrot", "quiz", "kim", "mango", "nature", "apple",
    "ball", "cat", "dog", "lime", "ruby", "shine", "tinkter",
    "ultra", "volly", "wow", "xerox", "yak", "zenon", "joke"}
    Output: Yes

    Input: keys[] = {"geeks", "for", "geeks"}
    Output: No
'''
from trie import Trie

def check(trie):
    for node in trie.root.children:
        if node is None:
            return False
    return True

keys = ["geeks", "for", "geeks"]

trie = Trie(26)
for key in keys:
    trie.insert(key)
print(check(trie))