#백준 1105
L,R=map(str,input().split())
count=0
for i in range(len(L)):
    if len(L)!=len(R):
        break
    if L[i]!=R[i]:
        break
    elif L[i]=='8' and R[i]=='8':
        count+=1
print(count)