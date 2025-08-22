# PY1014	GIẢI MÃ

# Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. 
# Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và 
# viết số lượng phía sau các chữ cái đó.

# Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1
# Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.
# Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.

# Input
# Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.

# Output
# Với mỗi test ghi ra xâu ký tự ban đầu.

# Ví dụ
# Input        |  Output
# 2
# A8           |  AAAAAAAA
# A2E1C4G3D1   |  AAECCCCGGGD

for _ in range(0, int(input())):
    str = input()
    result = ""
    for i in range(0, len(str)):
        char = str[i]
        if char.isdigit():
            result += str[i - 1] * (int(char) - 1)
        else:
            result += char
    print(result)
        