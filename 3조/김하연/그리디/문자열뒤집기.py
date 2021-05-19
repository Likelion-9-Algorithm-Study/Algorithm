a=input()
r0,r1=0,0
if a[0]=='1': r0+=1
else: r1+=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        if a[i+1]=='0': r1+=1
        else: r0+=1
print(min(r0,r1))

'''
a=input()
z,o,r0,r1=0,0,0,0
for i in a:
    if i=='0':
        z+=1
        if o>0:
            r1+=1
            o=0
    else:
        o+=1
        if z>0:
            r0+=1
            z=0
if o>0: r1+=1
if z>0: r0+=1
print(min(r0,r1))
'''
