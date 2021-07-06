n = int(input())
coin = list(map(int,input().split()))
money = 1
coin.sort()
for c in coin:
    if money < c : break
    money+=c
print(money) 