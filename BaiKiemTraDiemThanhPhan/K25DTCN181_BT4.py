for test in range(int(input())):
    n = input().strip()

    first_two = n[:2]
    last_two = n[-2:]

    combined = first_two + last_two

    if combined == combined[::-1]:
        print("YES")
    else:
        print("NO")
