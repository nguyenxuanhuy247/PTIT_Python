# PY1010	ĐẦU CUỐI

# Viết chương trình kiểm tra xem số nguyên dương N 
# có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu 
# và hai chữ số cuối của nó thì sẽ tạo ra số có hai 
# chữ số giống nhau hay không?

# Input
# Dòng đầu ghi số số test (không quá 20). 
# Mỗi test là 1 số nguyên dương N có ít nhất 4 chữ số, 
# nhưng không quá 18 chữ số.

# Output
# Ghi ra YES hoặc NO

# Ví dụ
# Input             |   Output
# 3                 |
# 12321             |   NO
# 1234512           |   YES
# 10233211111       |   NO

for _ in range(int(input())):
    str = input()
    first = str[:2]
    last = str[-2:]
    
    print("YES") if(first == last) else print("NO")

