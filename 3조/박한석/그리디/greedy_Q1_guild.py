def make_guild(n, scare):
    scare.sort()  # 리스트 정렬 - O(NlogN)
    count = 0     # 만들어질 수 있는 guild의 수
    guild = []    # 길드
    flag = True
    while flag:
        if scare[0] <= n:
            guild = scare[:scare[0]]    # 우선 guild로 묶기
            print(guild)
            length = len(guild)

            # guild 내의 원소 유효성 검사(guild의 길이를 넘는 원소가 있는지를 check!)
            for i in range(length-1, -1, -1):   
                if guild[i] > length:   # 만약 guild의 길이를 넘는 원소가 있다면 False!
                    flag = False

            if flag == True:
                count += 1  # guild가 유효성 검사 통과한거니까 count 추가
                scare = scare[scare[0]:]  # slice (guild의 요소들은 다 제외.)
                n = len(scare)  # n update
            else:
                break # 해당 반복문을 탈출하므로 while문 탈출함!
        else:
            break
        
    print(count)
  
n = int(input())
scare = list(map(int, input().split()))

make_guild(n, scare)


# test case

# 5
# 1 7 8 9 9

# 5 
# 2 3 1 2 2

# 5
# 1 1 3 4 5

# 100
# 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2 7 8 9 1 2