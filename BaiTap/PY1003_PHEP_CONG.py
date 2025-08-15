# PY1003	PHÉP CỘNG

# Cho một phép toán có dạng a + b = c với a,b,c chỉ là các số nguyên dương có một chữ số.
# Hãy kiểm tra xem phép toán đó có đúng hay không.

# Input
# Chỉ có một dòng ghi ra phép toán (gồm đúng 9 ký tự)

# Ouput
# Ghi ra YES nếu phép toán đó đúng. Ghi ra NO nếu sai.

# Ví dụ
# Test 1
# Input
# 1 + 2 = 3
# Output
# YES

# Test 2
# Input
# 2 + 2 = 5
# Output
# NO

str = input().strip()
result = str.split()

if result[0].isdigit() and result[1] == '+' and result[2].isdigit() and result[3]  == '=' and result[4].isdigit() and (int(result[0]) + int(result[2]) == int(result[4])):
    print("YES")
else :
    print("NO")
