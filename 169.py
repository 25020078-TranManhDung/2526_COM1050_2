class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #Sắp xếp các phần tử
                    #do khi sắp xếp các ptu xuất hiện nhiều luôn xuất hiện ổ giữa mảng
        n = len(nums)
        return nums[n//2]       #trả về vị trí ở giữa mảng
        