# PY3002	Đếm Tần Suất Ước Số

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    max_A = max(A)
    freq = [0] * (max_A + 1)
    for num in A:
        freq[num] += 1

    divisor_count = {}
    for k in range(1, max_A + 1):
        count = 0
        for multiple in range(k, max_A + 1, k):
            count += freq[multiple]
        if count > 0:
            divisor_count[k] = count

    output = '{' + ', '.join(f'{k}: {v}' for k, v in divisor_count.items()) + '}'
    print(output)