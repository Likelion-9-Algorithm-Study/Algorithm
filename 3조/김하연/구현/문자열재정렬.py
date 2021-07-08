n = input()
alpha, num = [], []
for i in n:
    if i.isalpha(): alpha.append(i)
    else: num.append(i)
alpha.sort()
for i in alpha: print(i,end='')
print(sum(list(map(int,num))))