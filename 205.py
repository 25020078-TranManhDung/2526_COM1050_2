def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
        ST = {}
        TS = {}
        for S,T in zip(s,t):
            if S in ST:
                if ST[S] != T:
                    return False
            else:
                ST[S] = T
            if T in TS:
                if TS[T] != S:
                    return False
            else:
                TS[T] = S
    return True
s = input("Nhập s: ")
t = input("Nhập t: ")
print(isIsomorphic(s, t))        