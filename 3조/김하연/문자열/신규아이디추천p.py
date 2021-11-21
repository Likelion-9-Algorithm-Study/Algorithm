import re


def solution(new_id):
    n = new_id.lower()
    a = []
    for i in n:
        if i.isalpha() or i.isdecimal() or i in ['-', '_', '.']:
            a.append(i)
    n = re.sub('[.]+', '.', ''.join(a))
    if n != '':
        try:
            if n[0] == '.': n = n[1:]
            if n[-1] == '.': n = n[:-1]
        except:
            n = ''
    if n == '': n += 'a'
    if len(n) >= 16:
        n = n[:15]
        if n[-1] == '.':
            n = n[:-1]
    if len(n) <= 2:
        while len(n) < 3:
            n += n[-1]

    return n