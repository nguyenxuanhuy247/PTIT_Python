import math

def euclidean(v1, v2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(v1, v2)))

def manhattan(v1, v2):
    return sum(abs(x - y) for x, y in zip(v1, v2))

def minkowski(v1, v2, p=3):
    return sum(abs(x - y) ** p for x, y in zip(v1, v2)) ** (1 / p)

def jaccard(v1, v2):
    set1, set2 = set(v1), set(v2)
    if not set1 and not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

for test in range(int(input())):
    distance_type = input().strip().lower()
    
    try:
        v1 = list(map(float, input().split()))
        v2 = list(map(float, input().split()))
    except:
        print("Invalid")
        continue

    # Kiểm tra độ dài vector
    if len(v1) != len(v2):
        print("Invalid")
        continue

    # Tính khoảng cách dựa trên loại
    if distance_type == 'euclidean':
        result = euclidean(v1, v2)
    elif distance_type == 'manhattan':
        result = manhattan(v1, v2)
    elif distance_type == 'minkowski':
        result = minkowski(v1, v2, p=3)
    elif distance_type == 'jaccard':
        result = jaccard(v1, v2)
    else:
        print("Invalid")
        continue

    print(f"{result:.5f}")
