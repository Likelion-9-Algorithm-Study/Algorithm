n, m = map(int,input().split())
weight = list(map(int,input().split()))
count = 0

for i in range(n):
    for j in range(i+1,n):
        if weight[i]!=weight[j]: count+=1

print(count)

'''
array = [0]*(m+1)
for x in weight:
    array[x]+=1
result = 0
for i in range(1,m+1):
    n-= array[i]
    result += array[i]*n
print(result)
'''