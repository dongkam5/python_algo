n=int(input())

cnt=0
name=[0 for _ in range(26)]
ans=[]
for i in range(n):
    a=input()
    name[ord(a[0])-97]+=1

for i in range(26):
    if name[i]>=5:
        alphabet=chr(i+97)
        ans.append(alphabet)
        cnt+=1

if cnt!=0:
    print(''.join(ans))
else:
    print("PREDAJA")