#프로그래머스 최댓값과 최솟값
def solution(s):
    lst=list(map(int,s.split()))
    m=str(min(lst))
    M=str(max(lst))
    answer='{} {}'.format(m,M)
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))