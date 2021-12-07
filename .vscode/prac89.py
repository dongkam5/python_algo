#백준 4796

lst=list(map(str,input()))

ans=['U','C','P','C']
iteration=0
for i in lst:
    if i==ans[iteration]:
        iteration+=1
    if iteration==4:
        break

if iteration==4:
    print('I love UCPC')
else:
    print('I hate UCPC')