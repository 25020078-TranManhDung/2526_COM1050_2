class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):        #dùng and thì khi 1 xâu hết ký tự để them vào thì vòng while kết thúc
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])                           #thêm các ptu còn lại của chuỗi sau khi vòng while kết thúc, các ptu thêm sẽ bắt đầu từ ptu thứ i trở đi
                                                        # [i:]  : tính từ i
        res.append(word2[j:])
        return "".join(res)
        