def reverseIndividualWords(s):
    st = []
    for c in s:
        if c ==' ':
            while len(st) > 0:
                print(st.pop(), end="")
            print(" ", end="")
        else:
            st.append(c)
    while len(st) > 0:
        print(st.pop(), end="")
    print()


s = "GeeksforGeeks is good to learn"
reverseIndividualWords(s)
