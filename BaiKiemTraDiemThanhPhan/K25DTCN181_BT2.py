for test in range(int(input())):
    s = input().strip()

    odd = 1
    sum = 0

    for i, ch in enumerate(s, start = 1):
        digit = int(ch)
        if i % 2 == 1:
            odd *= digit
        else:
            sum += digit
    
    if sum == 0:
        print("INVALID")
    else:
        result = odd / sum
        print(f"{result:.6f}")