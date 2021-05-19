def plus_or_multiply(array):
    result = array[0]   # base case
    for i in range(1, len(array)):
        # base case가 0 or 1이거나 다음 값이 0 or 1 일 때.
        if result == 0 or result == 1 or array[i] == 0 or array[i] == 1:
            result += array[i]
        else: # 0 or 1이 아닐 때
            result *= array[i]

    return result

n = input()
arr = []
for i in n:
    arr.append(int(i))

print(plus_or_multiply(arr))

# test case

# 0001324

# 1323400