#프로그래머스 등굣길
def solution(m, n, puddles):
    answer = 0
    field=[[0]*(m) for _ in range(n)]
    field[0][0]=1
    for puddle in puddles:
        y=puddle[0]
        x=puddle[1]
        field[x-1][y-1]=-1
    i=0
    while i<m:
        if field[0][i]==-1:
            break
        else:
            field[0][i]=1
            i+=1
    i=0
    while i<n:
        if field[i][0]==-1:
            break
        else:
            field[i][0]=1
            i+=1
    if n==1:
        if field[0][m-1]==1:
            answer=1
            return answer
        else:
            answer=0
            return answer
    elif m==1:
        if field[n-1][0]==1:
            answer=1
            return answer
        else:
            answer=0
            return answer
    else:
        for i in range(1,n):
            for j in range(1,m):
                if field[i][j]!=-1:
                    if field[i-1][j]==-1 and field[i][j-1]==-1:
                        pass
                    elif field[i-1][j]==-1:
                        field[i][j]=field[i][j-1]%1000000007
                    elif field[i][j-1]==-1:
                        field[i][j]=field[i-1][j]%1000000007
                    else:
                        field[i][j]=(field[i-1][j]+field[i][j-1])%1000000007
    answer=field[n-1][m-1]
    return answer