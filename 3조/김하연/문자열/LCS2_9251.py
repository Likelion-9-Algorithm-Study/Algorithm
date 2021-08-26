import sys
f = sys.stdin.readline

str1 = ' ' + f().strip()
str2 = ' ' + f().strip()

result = [[''] * len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            result[i][j] = result[i-1][j-1] + str1[i]
        else:
            if len(result[i-1][j]) > len(result[i][j-1]):
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = result[i][j-1]

result = result[-1][-1]
print(len(result))
if len(result): print(result)

'''
ACAYKP
CAPCAK
'''