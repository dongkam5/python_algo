king,doll,num=map(str,input().split())
doll=list(doll)
king=list(king)
doll_column=ord(doll[0])-65
doll_row=int(doll[1])-1
king_column=ord(king[0])-65
king_row=int(king[1])-1

for i in range(int(num)):
    string=str(input())
    if string =='R':
        if (king_column+1)==doll_column and doll_column<=6:
         king_column+=1
         doll_column+=1
        elif (king_column+1)!=doll_column and king_column<=6:
            king_column+=1
    elif string =='L':
          if (king_column-1)==doll_column and doll_column>=1:
            king_column-=1
            doll_column-=1
          elif king_column-1!=doll_column and king_column>=1:
            king_column-=1
    elif string =='B':
        if king_row-1==doll_row and doll_row>=1:
            king_row-=1
            doll_row-=1
        elif king_row-1!=doll_row and king_row>=1:
            king_row-=1
    elif string =='T':
        if king_row+1==doll_row and doll_row<=6:
            king_row+=1
            doll_row+=1
        elif king_row+1!=doll_row and king_row<=6:
            king_row+=1
    elif string =='RT':
        if king_row+1==doll_row and king_column+1==doll_column and doll_row<=6 and doll_column<=6:
            king_column+=1
            king_row+=1
            doll_row+=1
            doll_column+=1
        elif king_row+1!=doll_row and king_column+1!=doll_column and king_row<=6 and king_column<=6:
            king_column+=1
            king_row+=1
         
    elif string =='LT':
        if king_row+1==doll_row and king_column-1==doll_column and doll_row<=6 and doll_column>=1:
            king_column-=1
            king_row+=1
            doll_row+=1
            doll_column-=1
        elif king_row+1!=doll_row and king_column-1!=doll_column and king_row<=6 and king_column>=1:
            king_column-=1
            king_row+=1
    elif string =='RB':
        if king_row-1==doll_row and king_column+1==doll_column and doll_row>=1 and doll_column<=6:
            king_column+=1
            king_row-=1
            doll_row-=1
            doll_column+=1
        elif king_row-1!=doll_row and king_column+1!=doll_column and king_row>=1 and king_column<=6:
            king_column+=1
            king_row-=1
    elif string =='LB':
        if king_row-1==doll_row and king_column-1==doll_column and doll_row>=1 and doll_column>=1:
            king_column-=1
            king_row-=1
            doll_row-=1
            doll_column-=1
        elif king_row-1!=doll_row and king_column-1!=doll_column and king_row>=1 and king_column>=1:
            king_column-=1
            king_row-=1

doll[0]=chr(doll_column+65)
doll[1]=str(doll_row+1)
king[0]=chr(king_column+65)
king[1]=str(king_row+1)
print(''.join(king))
print(''.join(doll))