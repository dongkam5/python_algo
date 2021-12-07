#프로그래머스 숫자의 표현

def solution(n):
    answer = 0
    for i in range(n,0,-1):
        val=n
        k=i
        while True:
            if val-k>0:
                val-=k
                k-=1
                if k==0:
                    break
            elif val-k==0:
                answer+=1
                break
            else:
                break
    return answer