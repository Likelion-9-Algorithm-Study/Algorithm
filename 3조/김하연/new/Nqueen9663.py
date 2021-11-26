import sys
f = sys.stdin.readline

n = int(f())

c = [0] * n
cnt = 0

flag_a=[False]*n
flag_b=[False]*(n+(n-1))
flag_c=[False]*(n+(n-1))

def set(i):
    global cnt
    for j in range(n):
        if not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+(n-1)]:
            c[i] = j
            if i == n-1:
                cnt += 1
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+(n-1)]=True
                set(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+(n-1)]=False
set(0)
print(cnt)
