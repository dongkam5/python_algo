#백준 20300
n=int(input())
lst=list(map(int,input().split()))
lst.sort()
leng=len(lst)
M=0
if leng%2==0:
    for i in range (leng//2):
        M=max(M,lst[i]+lst[leng-1-i])
else:
    for i in range (leng//2):
        M=max(M,lst[i]+lst[leng-2-i])
    M=max(M,lst[leng-1])

print(M)