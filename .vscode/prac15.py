n=int(input())

stack=[]
ans=[]
for i in range(n):
    success=True
    string=list(map(str,input()))
    for j in string:
        if j=='(':
            stack.append(1)
        elif j==')':
            if (len(stack))==0:
                success=False
                break
            else:
                stack.pop()
    if success==True and (len(stack))==0:
        ans.append("YES")
    else:
        ans.append("NO")
    stack.clear()

for i in ans:
    print(i)



