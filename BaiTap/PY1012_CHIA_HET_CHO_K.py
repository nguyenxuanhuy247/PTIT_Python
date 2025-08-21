# PY1012	CHIA HẾT CHO K

# Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
# a + b ≤ N
# a + b chia hết cho K

# Input
# Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).

# Output
# Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.
# Nếu không tìm được số nào in ra -1

# Ví dụ
# Input         |   Output
# 10 1 10       |   -1
# 10 6 40       |   2 8 14 20 26

a, K, N = map(int, input().split())

res = []
start = ((a // K) + 1) * K - a 
if start <= 0:
    start += K
for b in range(start, N - a + 1, K):
    res.append(b)

if res:
    print(' '.join(map(str, res)))
else:
    print(-1)