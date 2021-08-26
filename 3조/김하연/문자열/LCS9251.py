import sys
f = sys.stdin.readline

str1 = ' ' + f().strip()
str2 = ' ' + f().strip()

result = [[0] * len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            result[i][j] = result[i-1][j-1] + 1
        else:
            result[i][j] = max(result[i-1][j], result[i][j-1])

print(result[-1][-1])