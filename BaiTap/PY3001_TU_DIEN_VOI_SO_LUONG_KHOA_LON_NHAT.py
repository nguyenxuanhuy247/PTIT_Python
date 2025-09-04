# PY3001	Từ điển với số lượng Khóa lớn nhất

# Mô tả:
# Cho một danh sách các dictionary (từ điển), mỗi dictionary có một số cặp khóa - giá trị (key-value pairs). 
# Nhiệm vụ của bạn là tìm dictionary có số khóa nhiều nhất và in ra số lượng khóa đó.
# Nếu có nhiều dictionary cùng số lượng khóa lớn nhất, bạn chỉ cần in ra số lượng khóa đó.

# Input:
# Dòng đầu tiên chứa một số nguyên N (1 ≤ N ≤ 1000), số lượng dictionary trong danh sách.
# Tiếp theo là N dòng, mỗi dòng là một dictionary được biểu diễn dưới dạng các cặp khóa và giá trị theo định dạng:
# key1:value1,key2:value2,...
# (Các khóa và giá trị được nối với nhau bằng dấu “:”, các cặp cách nhau bằng dấu “,”.
# Khóa là chuỗi không chứa dấu “:”, , và không có khoảng trắng.
# Giá trị là số nguyên trong khoảng [-10^9, 10^9].)

# Output:
# Một số nguyên là số lượng khóa nhiều nhất trong danh sách.

# Ví dụ:
# Input             | Output
# 3                 |  
# a:2,b:4           | 
# a:2,b:3,c:4,d:9   | 4
# a:2               | 

max_keys = 0

for _ in range(int(input())):
    line = input().strip()
    if line == '':
        num_keys = 0
    else:
        num_keys = len(line.split(','))
    if num_keys > max_keys:
        max_keys = num_keys

print(max_keys)