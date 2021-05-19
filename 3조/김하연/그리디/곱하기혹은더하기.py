a=input()
r=int(a[0])
for i in range(1,len(a)):
    b=int(a[i])
    if b<=1 or r<=1: r+=b
    else: r*=b
print(r)
