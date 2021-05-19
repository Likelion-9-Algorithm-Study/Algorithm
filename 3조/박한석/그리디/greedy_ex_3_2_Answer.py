# 실전문제 (큰 수의 법칙) (예시 답안) (가장 큰 수가 더해지는 횟수에 집중, 반복되는 부분 활용)

def find_large_numbers(n, m, k, arr):
    max_number = max(arr)
    arr.pop(arr.index(max_number))
    next_number = max(arr)
    final_num = 0

    count = (m // (k+1)) * k
    count += m % (k+1)

    final_num += count * max_number   
    final_num += (m-count) * next_number 

    print(final_num)


n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

find_large_numbers(n, m, k, arr)