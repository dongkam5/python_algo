#백준 1439

lst=list(map(int,input()))
d=0
bit=True
if lst[0]==0:
    bit=True
else:
    bit=False
for i in range(1,len(lst)):
    if lst[i]==0 and bit==False:
        d+=1
        bit=True
    elif lst[i]==1 and bit==True:
        d+=1
        bit=False

print((d+1)//2)

''' 다른풀이
S = input()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count + 1) // 2)
'''