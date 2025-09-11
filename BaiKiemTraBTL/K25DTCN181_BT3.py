def count_tg(arr):
    arr.sort()
    n = len(arr)
    count = 0
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if arr[i] + arr[j] > arr[k]:
                count += (j - i)
                j -= 1
            else:
                i += 1
    return count

t = int(input())
for test in range(int(t)):
    line = list(map(int, input().split()))
    print(count_tg(line))

