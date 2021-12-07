from sys import stdin

stack_l = list(stdin.readline().strip())
stack_r=[]

n=int(input())

for _ in range(n):
    temp = stdin.readline()
    if temp[0]=='L':
        if len(stack_l)==0:
            continue
        stack_r.append(stack_l.pop())
    elif temp[0]=='R':
        if len(stack_r)==0:
            continue
        stack_l.append(stack_r.pop())
    elif temp[0]=='B':
        if len(stack_l)==0:
            continue
        stack_l.pop()
    elif temp[0]=='P':
        stack_l.append(temp[2])

stack_l.extend(stack_r[::-1])
print(''.join(stack_l))