def flip_string(array):
    count_0 = 0     # 전체를 0으로 만들기
    count_1 = 0     # 전체를 1으로 만들기
    for i in range(len(array)-1):
        if array[i] == "1":
            if array[i+1] == "0" or (i+1) == (len(array)-1):
                count_0 += 1

            if array[i+1] == "0" and (i+1) == (len(array)-1):
                count_1 += 1
            

        if array[i] == "0":
            if array[i+1] == "1" or (i+1) == (len(array)-1):
                count_1 += 1

            if array[i+1] == "1" and (i+1) == (len(array)-1):
                count_0 += 1    
    
    result = min(count_0, count_1)
    print(result)

n = input()
arr = []
for i in n:
    arr.append(i)
flip_string(arr)


# test case

# 101010

# 010101

# 1100001


# 기발한 코드
# string = input()
# zero_split = len([s for s in string.split('0') if s])
# one_split = len([s for s in string.split('1') if s])

# print(zero_split) if zero_split < one_split else print(one_split)