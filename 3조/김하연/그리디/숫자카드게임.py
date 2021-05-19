a,b = map(int,input().split())
c,d=[],0
for i in range(a):
    c.append(list(map(int,input().split())))
    t=min(c[i])
    d=max(t,d)
print(d)
