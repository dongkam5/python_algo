#백준 1213
lst=list(map(str,input()))
lst.sort()
s1=[]
s2=[]

if len(lst)%2==0:
    while len(lst)!=0:
        s1.append(lst.pop(0))
        s2.append(lst.pop(0))
else:
    while len(lst)!=1:
        s1.append(lst.pop(0))
        s2.append(lst.pop(0))
    s1.append(lst.pop(0))
s2.reverse()
lst=s1+s2

print(lst)