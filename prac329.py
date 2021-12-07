#프로그래머스 다음 큰 숫자

def solution(n):
    bit=list(map(int,bin(n)[2:]))
    one_cnt=bit.count(1)
    i=n+1
    while True:
        cnt=list(map(int,bin(i)[2:])).count(1)
        if cnt==one_cnt:
            break
        i+=1
    answer=i
    return answer
