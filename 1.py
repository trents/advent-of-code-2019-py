with open('1.txt') as f:
    lines = f.readlines()

result = 0

for line in lines:
    temp = int(line.strip()) // 3 - 2
    result += temp

print("1a ->", result)

result = 0

for line in lines:
    temp = int(line.strip()) // 3 - 2
    result += temp
    while temp > 0:
        temp = temp // 3 - 2
        if temp > 0:
            result += temp

print("1b ->", result)
