#백준 10820
import sys
while True:

    lst=sys.stdin.readline().rstrip('\n')
    if not lst:
        break
    l=0
    u=0
    d=0
    b=0
    for i in lst:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
        elif i.isdigit():
            d+=1
        elif i.isspace():
            b+=1
    print(l,u,d,b)
