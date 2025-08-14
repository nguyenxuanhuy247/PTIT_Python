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

import math

def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    k = euler_phi(n)
    print("YES" if is_prime(k) else "NO")
