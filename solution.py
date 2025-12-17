def searchRange(nums, target):
        n = len(nums)
        l, r = 0, n - 1
        idx = [-1, -1]
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                left_mid = mid
                while (left_mid > 0) and (nums[left_mid-1] == target):
                    left_mid -= 1
                right_mid = mid
                while (right_mid < n - 1) and (nums[right_mid+1] == target):
                    right_mid += 1
                idx = [left_mid, right_mid]
                return idx  
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return idx