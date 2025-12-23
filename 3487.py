class Solution:
    def maxSum(self, nums: List[int]) -> int:
        am = []
        duong = []
        co_so_duong = False
        for i in nums:
            if i <= 0:
                am.append(i)
            elif i > 0:
                co_so_duong = True
                if i in duong:
                    continue
                else:
                    duong.append(i)
        if co_so_duong == True:
            return sum(duong)
        return max(am)