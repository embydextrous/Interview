# Russian Pheasant
# Trie
# Manacher
# Booth
# Finite Automata

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = computeLPSArray(pat)
    i = 0 # index for txt[]
    j = 0 # index for pat[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat):
    M = len(pat)
    length = 0 # length of the previous longest prefix suffix
    i = 1
    lps = [0] * M
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps
  
txt = "XBABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
print(computeLPSArray("AABBAA"))