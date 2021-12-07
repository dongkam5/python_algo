#프로그래머스 소수 찾기

def solution(numbers):
    import sys
    import math
    sys.setrecursionlimit(10**6)
    answer = 0
    numbers=list(map(str,numbers))
    leng=len(numbers)
    lst=[]
    visited=[0]*(leng)
    def is_prime_number(x):
      for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
          return False
      return True
    def dfs(val):
        value=int(val)
        if value not in lst:
            if is_prime_number(value):
              if value != 1 and value != 0:
                  lst.append(value)
                  print(lst)
        for i in range(leng):
            if visited[i]==0:
                visited[i]=1
                dfs(val+numbers[i])
                visited[i]=0
    for i in range(leng):
        num=int(numbers[i])
        if num not in lst:
            if num==2 or num==3 or num==5 or num==7:
                lst.append(num)
        visited[i]=1
        dfs(numbers[i])
        visited[i]=0
    answer=len(lst)
    return answer
