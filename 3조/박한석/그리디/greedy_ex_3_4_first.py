def make_one(n, k):
    count = 0
    while n > 1:
        if n % k == 0: # k ≥ 2
            count += 1
            n = n//k
            if n == 1:
                break
        else:
            n -= 1
            count += 1
    return count

n, k = map(int, input().split())
print(make_one(n, k))