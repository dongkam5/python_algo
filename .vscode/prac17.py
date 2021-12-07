from sys import stdin

n=int(input())
Queue=[]
ans=[]
for i in range(n):
    command=stdin.readline()
    if 'push' in command:
        a,b=map(str,command.split())
        Queue.append(b)
    elif 'pop'in command:
        if len(Queue)==0:
            ans.append(-1)
        else:
            ans.append(Queue.pop(0))
    elif 'size' in command:
        ans.append(len(Queue))
    elif 'empty' in command:
        if len(Queue)==0:
            ans.append(1)
        else:
            ans.append(0)
    elif 'front' in command:
        if len(Queue)==0:
            ans.append(-1)
        else: ans.append(Queue[0])
    elif 'back' in command:
        if len(Queue)==0:
            ans.append(-1)
        else: ans.append(Queue[-1])

for i in ans:
    print(i)