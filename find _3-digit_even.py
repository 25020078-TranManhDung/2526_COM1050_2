from collections import Counter

def findEvenNumbers(digits):
    counts = Counter(digits)                            #dùng counter để đếm số lần xuất hiện của ptu trong mảng
    results = []                                        #res để lưu các số thoả mãn

    def backtrack(step, current_num):                   #tạo hàm đệ quy, step nhằm chỉ các bước chọn hàng trăm(0), chục(1), đơn vị(2)
        if step == 3:                                   #step = 3 tức là đã chọn được cả 3 hàng
            if current_num % 2 == 0:                    #kiểm tra xem số đó có chẵn ko (thực chất đã kiểm tra ở bước dưới)
                results.append(current_num)             #thêm số thoả mãn vào mảng
            return
        
        for d in range(10):                             #lặp từ 0 -> 9 để chọn số
            if counts[d] > 0:                           #nếu có số trong mảng và còn số để chọn
                if step == 0 and d == 0:                #kiểm tra điều kiện hàng trăm nếu d = 0 thì loại
                    continue
                if step == 2 and d % 2 != 0:            #kiểm tra điều kiện hàng đơn vị phải là só chẵn
                    continue

                counts[d] -= 1                          #khi chọn được số tm, ta mất 1 lần dùng số đó
                backtrack(step + 1, current_num * 10 + d)
                                                        #gọi đệ quy để tiếp tục tìm hàng tiếp theo với step + 1, curr_num nhân 10 + d(d1, d1*10 +d2, d1d2 *10 + d3) 
                counts[d] += 1                          #nếu th đệ quy ko tìm được số thoả mãn, phải trả về 1 lần dùng và thử nhánh khác
    backtrack(0,0)                                      #gọi đệ quy với step = 0, curr_num = 0

    return results              
    
digits = list(map(int, input("Nhập mảng: ").split()))
print(findEvenNumbers(digits))

