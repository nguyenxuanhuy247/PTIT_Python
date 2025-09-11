# PY2003	TÁCH DANH SÁCH THÀNH CÁC DANH SÁCH CON

def split_list(lst, k):
    return [lst[i:i+k] for i in range(0, len(lst), k)]

for _ in range(int(input().strip())):
    numbers = list(map(int, input().strip().split()))
    k = int(input().strip())

    if k >= len(numbers):
        print("INVALID")
    else:
        result = split_list(numbers, k)
        print(' '.join(str(sub) for sub in result))
