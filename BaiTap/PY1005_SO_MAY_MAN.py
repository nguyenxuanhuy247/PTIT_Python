# PY1005   SỐ MAY MẮN

# Chữ số 4 và chữ số 7 được xem là các chữ số may mắn.
# Cho số nguyên dương N có không quá 18 chữ số. Hãy đếm 
# xem số chữ số 4 cộng với số chữ số 7 trong N có phải 
# bằng 4 hay bằng 7 hay không.

# Input
# Chỉ có số N

# Output
# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ
# Input                     |  Output
# 40047                     |  NO
# 7747774                   |  YES
# 1000000000000000000       |  NO

count = 0
for char in input():
    if (char == '4' or char == '7') : 
        count += 1

print("YES") if (count == 4 or count == 7) else print("NO")