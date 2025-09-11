import json
with open('tips.json', 'r') as f:
    data = json.load(f)['tips']


t = int(input().strip())
for test in range(int(t)):
    day, time = input().split()
    tips = [float(record['tip']) for record in data if record['day'] == day and record['time'] == time]

    if tips:
        avg = sum(tips) / len(tips)
        print(f"{avg:.4f}")
    else:
        print("Invalid")