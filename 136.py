def singleNumber(nums):
    res = 0
    for i in nums:
        res = res ^ i
    return res

nums = list(map(int, input("nhập dãy số: ").split()))
print(singleNumber(nums))

        