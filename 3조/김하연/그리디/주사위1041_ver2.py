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

    min1 = dice[0]
    min2 = dice[0]+dice[1]
    min3 = dice[0]+dice[1]+dice[2]

    plane1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    plane2 = 4*(n-2) + 4*(n-1)
    plane3 = 4
    sum+=min1*plane1 
    sum+=min2*plane2
    sum+=min3*plane3

    print(sum)