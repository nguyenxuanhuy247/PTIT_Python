# PY1009	CHỮ HOA-CHỮ THƯỜNG

# Cho một xâu ký tự chỉ bao gồm các ký tự chữ cái, 
# độ dài không quá 100. Hãy thực hiện:

# Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái 
# viết thường lớn hơn hoặc bằng số lượng chữ cái viết hoa.
# Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết 
# hoa lớn hơn số lượng chữ cái viết thường.

# Input
# Chỉ có một xâu ký tự độ dài không quá 100, không có khoảng trống

# Output
# Ghi ra xâu kết quả

# Ví dụ
# Input         |   Output
# vietHoa       |   viethoa
# VIETTHuoNg    |   VIETTHUONG

str = input()
lowerNum = upperNum = 0
for ch in str:
    lowerNum += 1 if ch.islower() else 0
    upperNum += 1 if ch.isupper() else 0

print(str.lower()) if lowerNum >= upperNum else print(str.upper())
    