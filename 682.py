class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:                        #duyệt qua từng phần tử trong opts
            if i == "+":
                stack.append(stack[-1]+stack[-2])   #tính tổng xét các ptu đã có trong stack
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "C":
                stack.pop()                         #pop() xoá ptu
            else:
                stack.append(int(i))                #append(int(i)) do các số trong list là str
        return sum(stack)                           #trả về tổng các ptu trong stack
        