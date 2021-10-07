import sys
f = sys.stdin.readline

n = int(f())
crane = sorted(list(map(int, f().split())), reverse=True)
m = int(f())
box = sorted(list(map(int, f().split())), reverse=True)

def move():
    if crane[0] < box[0]:
        return -1
    ans = 0
    while len(box) > 0:
        ans += 1
        for c in crane:
            for i in range(len(box)):
                if c >= box[i]:
                    box.pop(i)
                    break
    return ans

print(move())

'''
time = 0 # 시간
checked = [0 for _ in range(m)] 
count = 0 

positions = [0] * n

if max(box) > max(crane):
    print(-1)
else:
    while count < len(box):
        for i in range(n):
            while positions[i] < len(box):
                if not checked[positions[i]] and crane[i] >= box[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        time += 1
    print(time)   
'''