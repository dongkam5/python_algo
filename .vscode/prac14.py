from sys import *
n=int(input())

lst=[]
ans=0
answer=[]
for i in range(n):
    string=stdin.readline()

    if 'push' in string:
       a,b=string.split()
       lst.append(b)
    elif 'pop' in string:
        if len(lst)==0:
            ans=-1
        else:
            ans=lst[-1]
            lst=lst[:-1]
        answer.append(ans)
    elif 'size' in string:
        ans=len(lst)
        answer.append(ans)
    elif 'empty' in string:
        if len(lst)==0:
            ans=1
        else:
            ans=0
        answer.append(ans)
    elif 'top' in string:
        if len(lst)==0:
            ans=-1
        else:
            ans=lst[-1]
        answer.append(ans)

for i in answer:
    print(i)