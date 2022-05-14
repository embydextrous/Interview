def removeConsecutiveWords(s):
    words = s.split()
    s = []
    while len(words) > 0:
        word = words.pop(0)
        if len(s) == 0 or s[-1] != word:
            s.append(word)
        else:
            s.pop()
    return " ".join(s)

a = "modi sushma sushma"
print(removeConsecutiveWords(a))