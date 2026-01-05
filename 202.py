def get_sum_of_squares(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit ** 2
        n //= 10
    return total_sum

def isHappy(n):
    num = set()
    while n != 1:
        if n in num:
            return False
        num.add(n)
        n = get_sum_of_squares(n)
    return True       

n = int(input("nhập số n: "))
print(isHappy(n))
