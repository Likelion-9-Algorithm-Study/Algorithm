n = int(input())
slime = list(map(int,input().split()))
slime.sort()
score = 0
for i in range(1,n):
    score+=slime[i-1]*slime[i]
    slime[i]+=slime[i-1]
print(score)