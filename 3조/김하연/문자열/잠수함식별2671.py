import sys
import re
f = sys.stdin.readline

sound = f().strip()
p = re.compile('(100+1+|01)+')
res = p.fullmatch(sound)
if res: print('SUBMARINE')
else: print('NOISE')