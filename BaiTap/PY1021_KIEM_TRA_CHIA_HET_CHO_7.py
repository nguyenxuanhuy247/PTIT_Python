# PY1021	KIỂM TRA CHIA HẾT CHO 7

# Cho một số nguyên dương N. Mỗi bước bạn thực hiện tính tổng của N 
# với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia 
# hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.
# Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên 
# hoặc ghi ra -1 nếu không thể tìm ra đáp án.

# Input:
# Dòng đầu ghi số bộ test (không quá 1000).
# Mỗi test ghi số N (1 ≤ N ≤ 1018)

# Output:
# Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.

# Ví dụ:
# Input             | Output
# 5                 | 
# 1                 | 77
# 2                 | 77
# 3                 | 9447438
# 4                 | 77
# 999999            | 999999

def findNumber(n):
    for t in range(1000):
        if int(n) % 7 == 0:
            return n
        n = str(int(n) + int("".join(list(reversed(n)))))

for t in range(int(input())):
    print(findNumber(input()))