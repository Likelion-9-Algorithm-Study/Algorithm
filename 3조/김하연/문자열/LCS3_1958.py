import sys
f = sys.stdin.readline

str1 = ' ' + f().strip()
str2 = ' ' + f().strip()
str3 = ' ' + f().strip()

result = [[[0] * len(str3) for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        for k in range(1, len(str3)):
            if str1[i] == str2[j] == str3[k]:
                result[i][j][k] = result[i-1][j-1][k-1] + 1
            else:
                result[i][j][k] = max(result[i-1][j][k], result[i][j-1][k], result[i][j][k-1])

print(result[-1][-1][-1])
