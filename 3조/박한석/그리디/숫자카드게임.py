def card_game(n, m, matrix):
    result_arr = []
    for i in range(n):
        result_arr.append(min(matrix[i]))   # 각 행의 최솟값들을 새로운 배열에 넣기

    print(max(result_arr))                  # 그 값들 중 최댓값을 뽑아내기

n, m = map(int, input().split())
matrix = []
for i in range(n): # make a 2D matrix
    matrix.append(list(map(int, input().split())))

card_game(n, m, matrix)