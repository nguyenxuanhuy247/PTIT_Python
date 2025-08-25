# PY1017	KIỂM TRA SỐ

# Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn 
# đồng thời hai tính chất sau đây hay không?
# Tổng chữ số của N chia hết cho 10
# Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng 
# số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ
# Input         |  Output
# 3
# 1353          |  NO
# 246864        |  YES
# 123435        |  NO


def tong(n):
    n = int(n)
    sum = 0
    while n != 0:
        sum += n %10
        n //= 10
    return sum

for _ in range(int(input())):
    str = input()
    i = 0
    while i < len(str) - 1 and abs(int(str[i]) - int(str[i + 1])) == 2:
        i += 1
    if i == len(str) - 1 and tong(str) % 10 == 0: print("YES")
    else: print("NO")