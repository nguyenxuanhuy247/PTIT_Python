# PY1013	SỐ KHÔNG GIẢM

# Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.
# Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.

# Input
# Dòng đầu ghi số bộ test (không quá 10).
# Mỗi dòng ghi một số nguyên dương (không quá 500 chữ số).

# Output
# Ghi ra YES nếu đó là số không giảm. NO nếu ngược lại

# Ví dụ
# Input                             |  Output
# 2
# 12345678888888888888889           |  YES
# 65645645465754765876857685846     |  NO

a, K, N = map(int, input().split())
found = False

for total in range(0, N + 1, K):
    if total > a:
        found = True
        print(total - a, end=' ')
        
if not found: print("-1")