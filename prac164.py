#백준 2491
import sys
n=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
m=1
M=1
m_count=1
M_count=1
for i in range(n-1):
    if lst[i]>lst[i+1]:
        M_count+=1
        m=max(m,m_count)
        m_count=1
    elif lst[i]<lst[i+1]:
        m_count+=1
        M=max(M,M_count)
        M_count=1
    else:
        M_count+=1
        m_count+=1
m=max(m,m_count)
M=max(M,M_count)
print(max(M,m))