n = int(input())
num = list(map(int,input().split()))
sum, dice = 0, []
if n==1:
    num.sort()
    for i in range(5):
        sum+=num[i]
    print(sum)
else:
    dice.append(min(num[0],num[5]))
    dice.append(min(num[1],num[4]))
    dice.append(min(num[2],num[3]))
    dice.sort()

    a = dice[0]*(n*n*2)
    b = dice[1]*(n*4) 
    c = dice[0]*((n*n*2) - (n*4))
    d = dice[2]*4
    e = dice[1]*(n-2)*4
    f = dice[0]*(n*n-((n-2)*4)-4)

    print(a+b+c+d+e+f)

