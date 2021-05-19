# 실전문제 (큰 수의 법칙)

def find_large_numbers(n, m, k, arr):
    max_number = max(arr)
    arr.pop(arr.index(max_number))
    next_number = max(arr)
    count = 0
    final_num = 0
    while m > 0:
        for i in range(k):
            if m < 1:
                break
            else:
                final_num += max_number
                # print('+', max_number)
                m -= 1
        if m < 1:
            break
        else:
            final_num += next_number
            # print('+', next_number)
            m -= 1
    print(final_num)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

find_large_numbers(n, m, k, arr)