# NGUYÊN TỐ

# Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất 
# của 2 số đó là 1. Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N 
# có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

# Input
# Dòng đầu ghi số bộ test, không quá 10.
# Dòng thứ 2 ghi số N (1 < N < 10000)

# Output
# Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ
# Input  |  Output
# 2      |  
# 2      |  NO
# 3      |  YES

from math import gcd, sqrt

def isPrime(x):
    if x < 2: return False
    elif x == 2: return True
    
    for i in range(3, sqrt(x) + 1, 2):
        if x %  i == 0: return False
    return True

for test in range(int(input())):
    n = int(input())
    count = 0
    
    for i in range(n):
        if gcd(i, n) == 1: count += 1
        
    print("YES") if isPrime(count) else print("NO")