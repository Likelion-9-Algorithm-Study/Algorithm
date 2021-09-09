import sys
f = sys.stdin.readline

n = int(f().strip())
string, d = [], {}

for _ in range(n):
    string.append(f().strip())

for i in string:
    for j in range(len(i)):
        if d.get(i[j]):
            d[i[j]] += 10 ** (len(i) - j - 1)
        else:
            d[i[j]] = 10 ** (len(i) - j - 1)

num = sorted(list(d.values()), reverse=True)

result, power = 0, 9

for x in num:
    result += x * power
    power -= 1

print(result)