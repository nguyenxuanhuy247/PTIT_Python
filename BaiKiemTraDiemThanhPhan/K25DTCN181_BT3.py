for test in range(int(input())):
    method = int(input().strip())
    full_name = input().strip()

    parts = [word.capitalize() for word in full_name.split()]

    if not parts:
        print("INVALID")
        continue

    if method == 1:
        last_name = parts[-1]
        remaining = parts[:-1]    
        print(f"{last_name} " + " ".join(remaining))
    elif method == 2:
        first_name = parts[0]
        remaining = parts[1:]    
        print(" ".join(remaining + [first_name]))