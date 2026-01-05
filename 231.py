def isPowerOfTwo(n):
        if n <= 0:
            return False
        if n == 1:
            return True
        return n % 3 == 0 and isPowerOfTwo(n//3)

n = int(input("Nhap so: "))
print(isPowerOfTwo(n))