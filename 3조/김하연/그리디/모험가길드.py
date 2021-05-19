n=int(input())
s=list(map(int,input().split()))
s.sort()

r,c=0,0

for i in s:
    c+=1
    if c>=i:
        r+=1
        c=0
print(r)