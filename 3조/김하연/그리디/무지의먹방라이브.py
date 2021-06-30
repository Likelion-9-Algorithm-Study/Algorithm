import heapq

def solution(food_times, k):
    if sum(food_times) <= k: return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    length = len(food_times)
    s, prev = 0,0
    while True:
        if s+((q[0][0]-prev)*length) <= k :
            current = heapq.heappop(q)[0]
            s+=(current-prev)*length
            length-=1
            prev = current
        else: break
    res = sorted(q, key=lambda x:x[1])
    return res[(k-s)%length][1]
    
        