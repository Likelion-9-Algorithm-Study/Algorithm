# https://www.acmicpc.net/problem/9663
def dfs(start):
    global result

    if start == n:
        result += 1
        return

    for i in range(n):
        flag = True
        for j in range(start):
            if board[j] == i or start - j == abs(i-board[j]):
                flag = False
                break
        if flag:
            board[start] = i
            dfs(start+1)


n = int(input())
result = 0
board = [0] * n
dfs(0)
print(result)