import sys
f = sys.stdin.readline

days = {1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
flowers = []
n = int(f())

for i in range(n):
    sm, sd, em, ed = map(int, f().split())
    flowers.append((days[sm] + sd, days[em] + ed))

dest, current = 334, 60
flowers.sort(key=lambda x:(x[0], x[1]))

idx, temp, flag, result = -1, 0, False, []

while current <= dest and idx < n:
    flag = False
    idx += 1
    for i in range(idx, n):
        if flowers[i][0] > current:
            break
        if temp < flowers[i][1]:
            temp = flowers[i][1]
            idx = i
            flag = True
    if flag:
        current = temp
        result.append(flowers[idx])
    else:
        result = []
        break

print(len(result))


