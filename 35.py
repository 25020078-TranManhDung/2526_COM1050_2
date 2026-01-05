def searchInsert(nums, target):
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

nums = list(map(int, input("nhập dãy số: ").split()))
target = int(input("nhập target: "))
print(searchInsert(nums, target))