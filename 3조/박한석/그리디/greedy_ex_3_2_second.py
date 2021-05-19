# 실전문제 (큰 수의 법칙) (규칙성 이용하기)

def find_large_numbers(n, m, k, arr):
    max_number = max(arr)
    arr.pop(arr.index(max_number))
    next_number = max(arr)
    final_num = 0

    if m // (k+1) > 0: # 반복되는 부분이 하나라도 생긴다면, 
        final_num += (max_number * k + next_number) * (m//(k+1))  #  반복되는 부분의 총합 * 반복 횟수
        m -= (m//(k+1)) * (k+1)   # 반복한 만큼을 m번에서 제외
    else:   # 반복한 부분을 제외하고는 더이상 반복을 하지 않으므로 아래의 for문을 통해 나머지를 채움
        # --- 한 묶음 ---  
        for i in range(k):
            if m >= 1:
                final_num += max_number
                m -= 1
            else:   # m < 1
                break
        # --- --- ---     
    print(final_num)

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

find_large_numbers(n, m, k, arr)