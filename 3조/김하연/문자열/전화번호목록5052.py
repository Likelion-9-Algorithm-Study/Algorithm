import sys
f = sys.stdin.readline

t = int(f())


def search(c):
    c.sort()
    for i in range(len(c)-1):
        if len(c[i]) < len(c[i+1]):
            if c[i+1].startswith(c[i]):
                return True
    return False


for _ in range(t):
    n = int(f())
    contact = []
    for i in range(n):
        contact.append(f().strip())
    if search(contact):
        print('NO')
    else:
        print('YES')
