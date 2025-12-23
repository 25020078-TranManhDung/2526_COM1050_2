class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1            #Tạo 2 con trỏ trái, phải
        while l < r:                    #khi trái còn nhỏ hơn phải
            s[l], s[r] = s[r], s[l]     #Tráo đổi vị trí trái phải
            l += 1                      #Thay đổi giá trị l,r để tiếp tục tráo đổi
            r -= 1
        return s
        