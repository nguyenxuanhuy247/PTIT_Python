# PY1016	SỐ LỘC PHÁT

# Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc. 
# Cho một số nguyên dương không quá 500 chữ số, hãy kiểm tra 
# số đó có phải số phát lộc hay không.

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi số nguyên dương cần kiểm tra (không quá 500 chữ số)

# Output
# Ghi ra kết quả kiểm tra tương ứng (YES hoặc NO)

# Ví dụ
# Input         |  Output
# 3
# 1539786       |  YES
# 1234789       |  NO
# 8686          |  YES

for _ in range(int(input())):
    str = input()
    i = 0
    length = len(str)
    print("YES") if str[length - 2] == '8' and str[length - 1] == '6' else print("NO")