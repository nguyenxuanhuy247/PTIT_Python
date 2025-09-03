# PY1025	HÌNH CHỮ NHẬT

# Cho độ dài hai cạnh của hình chữ nhật. Giá trị không quá 104.  
# Viết chương trình tính chu vi và diện tích của hình chữ nhật đó. 
# Nếu dữ liệu không hợp lệ (chiều dài hoặc chiều rộng ≤ 0 thì in ra số 0) 

# Input
# Có duy nhất một dòng ghi hai số nguyên, cách nhau một khoảng trống.

# Output
# In kết quả trên một dòng, chu vi rồi đến diện tích, cách nhau một khoảng trống.

# Ví dụ:
# Input             | Output
# 10 2              | 24 20 

a, b = map(int, input().split())

if a <= 0 or b <= 0:
    print(0)              
else:
    print(2 * (a + b), a * b)