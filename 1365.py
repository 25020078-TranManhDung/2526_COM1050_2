class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(len(nums)):
            count = 0
            l = i - 1
            r = i + 1
            while l >= 0:
                if nums[l] < nums[i]:
                    count += 1
                l -= 1
            while r < n:
                if nums[r] < nums[i]:
                    count += 1
                r += 1
            res.append(count)
        return res
    
        
