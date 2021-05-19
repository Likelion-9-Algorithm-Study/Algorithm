# https://www.acmicpc.net/problem/1439

a = input()
b = list(map(int, list(str(a))))

count_0, count_1 = 0, 0

for i in range(len(b)):
    if i == 0:
        if b[i] == 0:
            count_0 += 1
        else:
            count_1 += 1  # 처음에 0인지 1인지에 따라 숫자가 바뀌는 횟수를 카운트
    else:
        if b[i-1] != b[i]:
            if b[i-1] == 0:
                count_1 += 1
            else:
                count_0 += 1

if count_0 > count_1:
    print(count_1)
else:
    print(count_0)

 # 이전 항과 다른데 전 항이 0이면 이제 1로 바뀐 것이므로 이 때에 count_1(1로 바뀌는 지점)을 1 더해줌
 # 반대로, 전 항이 1이면 이제 0이 된 것이므로 이 때에 count_0(0으로 바뀌는 지점)을 1 더해줌
