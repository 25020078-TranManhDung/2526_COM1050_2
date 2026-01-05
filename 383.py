def canConstruct(ransomNote, magazine):
    d = {}
    for i in magazine:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in ransomNote:
        if j not in d or d[j] <= 0:
            return False
        d[j] -= 1
    return True

ransomNote = input("nhập ransomNote: ")
magazine = input("nhập magazine: ")
print(canConstruct(ransomNote, magazine))
