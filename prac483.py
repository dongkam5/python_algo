#백준 1764 듣보잡
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
answer=[]
cant_listen={}
for _ in range(N):
    cant_listen_man=str(input().rstrip())
    cant_listen[cant_listen_man]=1

for _ in range(M):
    cant_see_man=str(input().rstrip())
    if cant_listen.get(cant_see_man):
        ans=cant_see_man
        answer.append(ans)

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])