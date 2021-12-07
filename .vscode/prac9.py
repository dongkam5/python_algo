x=int(input())
numcount=0
init_i=1

while numcount!=x:
    i=init_i
    count=-1
    complete =True
    while (i//10)!=0:
        if count < (i%10):
            count=(i%10)
        else:
            count=-1
            complete=False
            break
        i=i//10
    if i>count and complete!=False:
        count=i
    else:
        count=-1
    if count>0:
        numcount+=1
    init_i+=1

print(init_i-1)