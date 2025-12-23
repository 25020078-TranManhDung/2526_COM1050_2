class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):               #tạo thêm hàm để kiểm tra trường hợp phải bỏ đi 1 ký tự
            while l < r:                       #khi l<r
                if s[l] != s[r]:                #nếu xảy ra th khác nhau 
                    return False                #trả về false do đề bài chỉ cho bỏ 1 ký tự
                l += 1                          #nếu ko khác nhau thay đổi l, r tiếp tục ktra
                r -= 1
            return True                         #trả về true nếu đối xứng
         
        n = len(s)
        l, r = 0, n - 1                         #tạo 2 con trỏ để ktra 2 bên trái phải              
        while l < r:                            #khi trái còn nhỏ hơn phải
            if s[l] != s[r]:                    #nếu xảy ra trường hợp khác nhau, ta xét đến trường hợp phải bỏ đi 1 ký tự
                return (is_palindrome(l + 1, r) or is_palindrome(l, r - 1))                                             #việc thay l = l + 1 và r = r -1 nhằm bỏ qua ptu khác nhau
                                                # dùng or vì chỉ cần 1 th đúng do ta chỉ cần bỏ 1 ptu
            l += 1                              #nếu các ptu l,r ko khác nhau thì thay đổi l, r để tiếp tục kiểm tra
            r -= 1
        
        return True                             #trả về true trong th ban đầu xâu vốn đã đối xứng

        
    
        