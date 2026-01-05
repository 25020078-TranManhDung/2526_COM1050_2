def thirdMax(nums):
        first = None
        second = None
        third = None
        for num in nums:
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                 third = second
                 second = num
            elif third is None or num > third:
                 third = num
        return third != None
nums = list(map(int, input("Nhập dãy só: ").split()))
print(thirdMax(nums))
