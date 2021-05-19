# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 유형별 기출문제 2 곱하기 혹은 더하기

a = input()
b = list(map(int, list(str(a))))

result = 0

for i in range(len(b)):
    if b[i] == 0:
        continue
    else:
        if i == 0:
            result = b[i]
        elif i == 1:
            if b[i-1] == 0:
                result += b[i]
            else:
                result *= b[i]
        else:
            result *= b[i]

print(result)

# 시간 좀걸림
