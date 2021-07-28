import sys
r = sys.stdin.readline

N = int(r())
solution = list(map(int, r().split()))
solution.sort()

left, right, result = 0, N-1, []
answer = sys.maxsize * 10


while left < right:

    current = solution[left] + solution[right]
    if answer > abs(current):
        answer = abs(current)
        result = [solution[left], solution[right]]
    if current < 0:
        left += 1
    else:
        right -= 1


print(min(result), max(result))
