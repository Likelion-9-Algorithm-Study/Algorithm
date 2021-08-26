# https://www.acmicpc.net/problem/1701
def table(x):
    leng = len(x)
    table = [0] * len(x)
    j = 0
    for i in range(1, leng):
        while j > 0 and x[i] != x[j]:
            j = table[j-1]
        if x[i] == x[j]:
            j += 1
            table[i] = j
    return max(table)

original_str = input()
result = 0

for i in range(len(original_str)):
    sub_str = original_str[i:]
    result = max(result, table(sub_str))

print(result)
