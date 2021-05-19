a=list(map(int,input().split()))
b=list(map(int,input().split()))
s,m,k=0,a[1],a[2]
b.sort()
t=b[-1]
t2=b[-2]
while True:
    for i in range(k):
        if m==0: break
        else:
            s+=t
            m-=1
    if m==0: break
    s+=t2
    m-=1

print(s)

    