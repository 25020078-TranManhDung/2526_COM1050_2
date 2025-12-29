def plus_one(digits):
    n = len(digits)
    i = n - 1
    while i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        elif digits[i] == 9:
            digits[i] = 0
            i = i - 1
    return [1] + digits

digits = list(map(int, input("Nhập số: ").split()))
print(plus_one(digits))
        
