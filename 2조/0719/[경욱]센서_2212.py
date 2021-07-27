import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
board = list(map(int, input().split()))
board.sort()
# print(board)
check = []
for i in range(1, len(board)):
    temp = board[i] - board[i-1]
    # if temp > 0:
    # check.append(temp)
    check.append(temp)
check.sort()
print(sum(check[:n-k]))
