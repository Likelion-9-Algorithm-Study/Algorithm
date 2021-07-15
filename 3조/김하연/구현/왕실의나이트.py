location = input()
r = int(location[1])
c = int(ord(location[0])) - int(ord('a')) + 1

move = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt = 0
for m in move:
    next_r = r+m[0]
    next_c = c+m[1] 
    if next_c >=1 and next_c <= 8 and next_r >= 1 and next_r <= 8: cnt+=1
print(cnt)