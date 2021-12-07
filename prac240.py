#백준 11048 dp
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
field=[]
for _ in range(n):
    field.append(list(map(int,input().split())))

for i in range(1,m):
    field[0][i]+=field[0][i-1]
for i in range(1,n):
    field[i][0]+=field[i-1][0]
for i in range(1,n):
    for j in range(1,m):
        field[i][j]+=max(field[i-1][j],field[i][j-1],field[i-1][j-1])

print(field[n-1][m-1])