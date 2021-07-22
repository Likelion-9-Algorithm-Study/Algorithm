import sys, heapq
input = sys.stdin.readline

N = int(input())
number = []
for n in map(int,input().split()):
    heapq.heappush(number,n)
for i in range(1,N):
    for n in map(int,input().split()):
        heapq.heappush(number,n)
        heapq.heappop(number)
print(heapq.heappop(number))

'''
for i in range(N):
    number.append(list(map(int,input().split())))
# number = numpy.array(number).transpose()
number = list(map(list,zip(*number)))
number = sorted(number, key = lambda x : x[-1])
print(number)
def num(N):
    if N == 1: return number[-1][-1]
    r, c, count = -1, -1, 2
    if number[r-1][c] >= number[r][c-1]: 
        current = [r-1,c]
        prev = [r,c-1]
    else:
        current = [r,c-1]
        prev = [r-1,c]

    while True:
        r, c = current[0], current[1]
        if count == N:
            return number[r][c]
        if number[r-1][c] >= number[r][c-1]:    current = [r-1,c]
        else:   current = [r,c-1]
        if number[current[0]][current[1]] < number[prev[0]][prev[1]]:
            temp = current
            current = prev
            prev = temp
        count+=1

print(num(N))
'''