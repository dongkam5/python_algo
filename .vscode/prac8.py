string=list(map(str,input()))
string.append('.')
length= len(string)
count=0
complete=True
for i in range(length):
    if (string[i]=='X'):
        count+=1
    else:
        if count%4==0 and count>0:
            for j in range(i-count,i):
                string[j]='A' 
            count=0
        elif count%2==0 and count>0:
            for j in range(i-count,i-2):
               string[j]='A'
            string[i-1]='B'
            string[i-2]='B'
            count=0
        elif count>0:
            complete=False
            break
        else: pass
string=string[:length-1]
if complete==True:
    print(''.join(string))
else:
    print(-1)
              
