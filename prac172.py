#프로그래머스 순간이동

def solution(n):
    n=int(n)
    ans = 0
    while n!=1:
        if n%2==0:
            n/=2    
        else:
            k=n%2
            n-=k
            ans+=k
    return (ans+1)