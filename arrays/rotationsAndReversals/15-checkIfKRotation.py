def checkKRotation(s1, s2, k):
    n = len(s1)
    k %= n
    s1 += s1
    return s1[k:n+k] == s2

print(checkKRotation("amazon", "azonam", 3))