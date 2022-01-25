# Number of characters
D = 256

def rabinKarpSearch(text, pattern, prime):
    N = len(text)
    M = len(pattern)
    hashText = 0
    hashPattern = 0
    h = 1
    for i in range(M-1):
        h = (h * D) % prime
    # Calculate Hash of Pattern and 1st Text Window
    for i in range(M):
        hashText = (D * hashText + ord(text[i])) % prime
        hashPattern = (D * hashPattern + ord(pattern[i])) % prime
    # last pattern will start from N-M
    for i in range(N-M+1):
        if hashText == hashPattern:
            # When hash matches start comparing
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            if j==M-1:
                print("Pattern found at index " + str(i))
        if i < N-M:
            hashText = (D * (hashText - h * ord(text[i])) + ord(text[M+i])) % prime

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
 
# A prime number
q = 101
rabinKarpSearch(txt,pat,q)

                

