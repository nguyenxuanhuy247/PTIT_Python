# PY1019	TÁCH TỪ

# Nhập xâu ký tự S có độ dài không quá 100. 
# Một từ được định nghĩa là một dãy ký tự không có khoảng trống.  
# Hãy tách xâu S thành các từ, mỗi từ in trên một dòng.

# Input:
# Chỉ có một dòng ghi xâu S (độ dài không quá 100)

# Output:
# Ghi ra kết quả.

# Ví dụ:
# Input             | Output
# Tin hoc co so 2   | Tin
#                   | hoc
#                   | co
#                   | so
#                   | 2

print("\n".join(input().split()))