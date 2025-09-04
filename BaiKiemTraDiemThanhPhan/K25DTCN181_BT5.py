for test in range(int(input())):
    s = input().strip()

    zero_groups = s.split('1')
    max_zero_len = max(len(group) for group in zero_groups)

    print(max_zero_len)
