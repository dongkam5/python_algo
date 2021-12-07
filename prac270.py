#프로그래머스 소수찾기
def solution(n):
    answer = 0
    for i in range(2,n+1):
        check=0
        for k in range(2,int(i**0.5)+1):
            if i%k==0:
                check=1
                break
        if check==0:
            answer+=1
                
            
    return answer