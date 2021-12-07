n = int(input())

count = [0,0,0,0,0,0,0,0,0,0]

for k in range(1,n+1):
     while (k//10)!=0:
       count[(k%10)]+=1
       k=k//10
     count[k]+=1
print(count)

