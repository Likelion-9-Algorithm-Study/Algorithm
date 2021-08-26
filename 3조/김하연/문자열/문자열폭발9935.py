import sys
f = sys.stdin.readline

string = f().strip()
bomb = f().strip()

result = []

for s in string:
    result.append(s)
    if s == bomb[-1] and ''.join(result[-len(bomb):]) == bomb:
        del result[-len(bomb):]

result = ''.join(result)

if result == '': print('FRULA')
else: print(result)
