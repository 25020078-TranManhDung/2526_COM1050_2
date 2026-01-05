def isSubsequence(s, t):
    i, j = 0, 0
    if s == []:
        return True
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

s = input("nhập dãy s: ")
t = input("nhập dãy t: ")
print(isSubsequence(s,t))
