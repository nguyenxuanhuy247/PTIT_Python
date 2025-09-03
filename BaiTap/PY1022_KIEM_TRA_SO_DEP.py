# PY1022	KIỂM TRA SỐ ĐẸP

# Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau 
# và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …

# Viết chương trình kiểm tra một số có phải số đẹp hay không?

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi một số nguyên dương N 
# (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.

# Output
# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ:
# Input             | Output
# 3                 | 
# 12121212          | YES
# 343433            | NO
# 78789989          | NO

def isLuckyNumber(n):
    for i in range(0, len(n) - 3):
        if n[i] == n[i+1] or n[i] != n[i+2]: 
            return 'NO'
    return 'YES'

for t in range(int(input())):
    print(isLuckyNumber(input()))