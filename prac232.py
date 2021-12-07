#백준 1057
N,A,B=map(int,input().split())
k=2
A-=1
B-=1
count=1
while True:
    if A//k == B//k:
        break
    else:
        count+=1
        k*=2

print(count)