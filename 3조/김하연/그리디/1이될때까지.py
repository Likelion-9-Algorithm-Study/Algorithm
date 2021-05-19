a,b=map(int,input().split())
c=0
while True:
    if a%b==0: a//=b
    else: a-=1
    c+=1
    if a==1: break
print(c)


