def solution(n):
    cnt = 0
    answer = 0
    while cnt != n:
        cnt+=1
        answer += 1
        while answer %3 == 0 or "3" in str(answer):
            answer += 1
    return answer