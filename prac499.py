#프로그래머스 level2 디펜스 게임 (재귀)
import sys
limit_number = 10**6
sys.setrecursionlimit(limit_number)
def solution(n, k, enemy):
    global answer
    global check
    answer = -1
    check = False
    combat(n,k,enemy,0)
    if check==True:
        return len(enemy)
    else:
        return answer

def combat(n,k,enemy,round_):
    global answer
    global check
    if round_==len(enemy):
        check=True
        return
    if n>=enemy[round_]:
        if k>0:
            combat(n,k-1,enemy,round_+1)
            combat(n-enemy[round_],k,enemy,round_+1)
        else:
            combat(n-enemy[round_],k,enemy,round_+1)
    else:
        if k>0:
            combat(n,k-1,enemy,round_+1)
        else:
            answer=max(answer,round_) 

print(solution(5,0,[1,1,1,1,1,1,1]))