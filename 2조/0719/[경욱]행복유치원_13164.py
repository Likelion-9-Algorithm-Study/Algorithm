import sys
input = sys.stdin.readline
n,k = list(map(int,input().split()))
board = list(map(int,input().split()))
check = []
for i in range(len(board)-1):
    check.append(board[i+1]- board[i])
check.sort()
print(sum(check[:n-k]))


# 질문 : 한명인조는 왜 비용 검사 안함...?
