def containsNearbyDuplicate(nums, k):
    d = {}
    for i, num in enumerate(nums):
        if num in d and i - d[num] <= k:
            return True
        else:
            d[num] = i
    return False

nums = list(map(int, input("Nhập dãy số: ").split()))
k = int(input("Nhập số: "))
print(containsNearbyDuplicate(nums, k))