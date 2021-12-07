#프로그래머스 점프와 순간 이동

def solution(n):
    ans = 0
    while n!=0:
        while n%2==0:
            n=n//2
        n-=1
        ans+=1
    return ans