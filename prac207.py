#백준 2210
import sys
sys.setrecursionlimit(10**6)
field=[]
for _ in range(5):
    field.append(list(map(str,sys.stdin.readline().split())))
lst=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def dfs(h,w):
    if len(string)==6:
        lst.append(''.join(string))
        return
    else:
        string.append(field[h][w])
        for i in range(4):
            q=w+dx[i]
            s=h+dy[i]
            if 0<=q<5 and 0<=s<5:
                dfs(s,q)
        string.pop()

for i in range(5):
    for j in range(5):
        string=[]
        dfs(i,j)
lst=set(lst)
lst=list(lst)
print(len(lst))