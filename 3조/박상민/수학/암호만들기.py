# https://www.acmicpc.net/problem/1759
from itertools import combinations

l, c = map(int, input().split())
al = {}
al_list = list(map(str, input().split()))
for i in range(len(al_list)):
    al[sorted(al_list)[i]] = i

result = []

vowels = 0
consonants = 0

for i in combinations(al, l):
    for j in i:
        if j in 'aeiou':
            vowels += 1
        else:
            consonants += 1

    if vowels >= 1 and consonants >= 2:
        print(*i, sep='')
    consonants = 0
    vowels = 0
