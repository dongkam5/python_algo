#백준 16173
import sys
n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    s=list(map(int,sys.stdin.readline().split()))
    lst.append(s)
check=0
def dfs(row,col,move):
    if move==-1:
        global check
        check=1
        return
    if move==0:
        return
    else:
        if move+row<=n-1:
            dfs(row+move,col,lst[row+move][col])
        if move+col<=n-1:
            dfs(row,col+move,lst[row][col+move])
dfs(0,0,lst[0][0])
if check==1:
    print('HaruHaru')
else:
    print('Hing')