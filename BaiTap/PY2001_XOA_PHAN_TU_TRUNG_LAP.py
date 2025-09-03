# PY2001	XÓA PHẦN TỬ TRÙNG LẶP

# Viết chương trình nhận vào một danh sách các số nguyên từ người dùng. 
# Xóa tất cả các phần tử trùng lặp, chỉ giữ lại lần xuất hiện đầu tiên 
# của mỗi phần tử, đồng thời giữ nguyên thứ tự ban đầu. In danh sách sau khi xử lý.

# Input:
# - Dòng thứ nhất ghi số phần tử k của danh sách
# - k dòng tiếp theo, mỗi dòng ghi một phần tử

# Output:
# Danh sách được xóa phần tử trùng lặp, mỗi phần tử cách nhau một dấu cách

# Ví dụ:
# Input             | Output
# 6                 |  
# 1                 |
# 2                 |
# 2                 | 1 2 3 4
# 3                 |
# 1                 |
# 4                 |

k = int(input())
nums = [int(input()) for _ in range(k)]

result = []
seen = set()

for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(' '.join(map(str, result)))
