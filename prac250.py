#백준 1991 트리
import sys
input=sys.stdin.readline
n=int(input())
tree=['.']*(1000000)
i=1
s=list(map(str,input().split()))
tree[1]=s[0]
tree[2]=s[1]
tree[3]=s[2]
for i in range(n-1):
    s=list(map(str,input().split()))
    tree[tree.index(s[0])*2]=s[1]
    tree[tree.index(s[0])*2+1]=s[2]
def leftdfs(i):
    print(tree[i],end='')
    if tree[2*i]!='.':
        leftdfs(2*i)
    if tree[2*i+1]!='.':
        leftdfs(2*i+1)

def middfs(i):
    if tree[2*i]!='.':
        middfs(2*i)
    print(tree[i],end='')
    if tree[2*i+1]!='.':
        middfs(2*i+1)

def rightdfs(i):
    if tree[2*i]!='.':
        rightdfs(2*i)
    if tree[2*i+1]!='.':
        rightdfs(2*i+1)
    print(tree[i],end='')
leftdfs(1)
print()
middfs(1)
print()
rightdfs(1)