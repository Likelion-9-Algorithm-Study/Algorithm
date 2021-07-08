n, l = list(map(int, input().split()))
loc = list(map(int, input().split()))
loc.sort()

count = 1 # 기존에 테이프가 최소 한 장은 붙여져 있다고 가정
start = loc[0]
end = start + l - 0.5  # 간격 0.5 있어야되니까 빼줌. 테이프의 끝 값이 end인 것임
for i in loc:
    if i > end:  # 테이프의 끝 값보다 크다면..
        count += 1  # 테이프가 한 개 더 필요하고
        end = i + l - 0.5  # 새로운 end는 start 대신에 i가 들어간다. i부터 다시 시작하기 때문

print(count)
