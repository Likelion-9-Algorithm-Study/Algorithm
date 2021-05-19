def make_one(n, k):
    result = 0

    while True:
        # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
        target = (n//k) * k
        result += (n - target)  # 나눠지지 않는 부분을 한 번에 뺌 (원래의 경우에선, 나누기 전에 빼는 경우랑 같음.)
        n = target
        # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
        if n < k:
            break
        # K로 나누기
        result += 1
        n //= k
    
    result += (n-1)  # 남은 부분 한 번에 빼주기
        
    print(result)

n, k = map(int, input().split())
print(make_one(n, k))