# PY2002	CẶP CÓ TỔNG SỐ BẰNG K

# Viết chương trình nhận vào một danh sách các số nguyên và một số nguyên k. 
# Tìm tất cả các cặp số trong danh sách có tổng bằng k và in ra các cặp đó. 
# Nếu không có cặp nào, thông báo không tìm thấy.
# Các cặp số được in ra theo thứ tự xuất hiện của số đầu tiên trong cặp

# Input:
# - Dòng đầu tiên ghi số bộ test
# Mỗi bộ test gồm 2 dòng
# - Dòng thứ nhất ghi danh sách, gồm các phần tử cách nhau bởi một hoặc nhiều dấu cách
# - Dòng tiếp theo ghi số k

# Output:
# Các cặp số tìm được theo format (a, b) trong đó a là số hạng đầu tiên. 
# Mỗi cặp số cách nhau bởi dấu cách. Nếu không tìm thấy in ra NO

# Ví dụ:
# Input             | Output
# 2                 |  
# 1 5 3   2  4      | 
# 7                 | (5, 2) (3, 4)
# 1 3 5 6 4 7       | 
# 20                | NO

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    k = int(input())

    pairs = [] 

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                pairs.append(f"({arr[i]}, {arr[j]})")

    if pairs:
        print(" ".join(pairs))
    else:
        print("NO")

