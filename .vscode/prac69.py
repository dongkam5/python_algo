#백준 11656
string=list(map(str,input()))
lst=[]
while len(string)!=0:
    lst.append(''.join(string))
    string.pop(0)
lst.sort()
for i in lst:
    print(i)