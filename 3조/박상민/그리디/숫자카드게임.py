# 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 그리디 실전문제 3번 숫자 카드 게임

n, m = map(int, input().split())

a = [0] * n
min_a = [0] * n

for i in range(n):
    a[i] = list(map(int, input().split()))
    min_a[i] = min(a[i])

print(max(min_a))

# 13분 걸림
