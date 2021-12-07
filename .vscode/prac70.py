#백준 11655
lst=list(map(str,input()))
for i in range(len(lst)):
    if lst[i].isupper():
        if (ord(lst[i])+13)>ord('Z'):
            lst[i]=chr(ord(lst[i])+13-26)
        else:
            lst[i]=chr(ord(lst[i])+13)
    elif lst[i].islower():
        if (ord(lst[i])+13)>ord('z'):
            lst[i]=chr(ord(lst[i])+13-26)
        else:
            lst[i]=chr(ord(lst[i])+13)
    else:
        pass
for i in lst:
    print(i,end='')