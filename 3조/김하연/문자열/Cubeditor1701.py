import sys

string = sys.stdin.readline().strip()
result = 0


def pi(sub):
    table = [0] * len(sub)
    j = 0
    for i in range(1, len(sub)):
        while j > 0 and sub[i] != sub[j]:
            j = table[j-1]
        if sub[i] == sub[j]:
            j += 1
            table[i] = j

    return max(table)


for i in range(len(string)):
    result = max(result, pi(string[i:]))

print(result)