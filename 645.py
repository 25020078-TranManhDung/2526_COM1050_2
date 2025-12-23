class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        dup = -1
        miss = -1
        for i in range(1, len(nums)+1):
            if i in count:
                if count[i] == 2:
                    dup = i
            else:
                miss = i
        return [dup, miss]