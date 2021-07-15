def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        string = ""
        prev =s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]: cnt+=1
            else:
                if cnt>1: string += str(cnt)+prev
                else: string += prev
                prev = s[j:j+i]
                cnt = 1
        if cnt>1: string+=str(cnt)+prev
        else: string += prev
        answer = min(answer, len(string))
    return answer
print(solution('abcabcdede'))