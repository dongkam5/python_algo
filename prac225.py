#백준 15803
import sys
input=sys.stdin.readline
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())

if a1==a2==a3 or b1==b2==b3:
    print('WHERE IS MY CHICKEN?')
else:
    try:
        if b3==(((b2-b1)/(a2-a1))*(a3-a2)+b2):
            print('WHERE IS MY CHICKEN?')
        else:
            print('WINNER WINNER CHICKEN DINNER!')
    except:
        print('WINNER WINNER CHICKEN DINNER!')