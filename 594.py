
def findLHS(nums):
    map = {}
    len = 0
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    for num in map:
        if num + 1 in map:
            len = max(len, map[num]+map[num+1])
    return len
    
nums = list(map(int, input("Nhap day so: ").split()))
print(findLHS(nums))
        