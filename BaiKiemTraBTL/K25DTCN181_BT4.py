from collections import OrderedDict

n = int(input().strip())
count = OrderedDict()

for _ in range(n):
    path = input()
    if not path or '/' not in path:
        continue

    msv = path.split('/')[0]
    count[msv] = count.get(msv, 0) + 1
    print(msv, count[msv])
