az=int(input())
bz=input()
c=[]
d=''
for i in (bz):
    if not(((i)=='a')or((i)=='e')or((i)=="i")or(i=="o")or(i=="u")or(i=="A")or(i=="E")or(i=="I")or(i=="O")or(i=="U")):
        c.append(i)
c.reverse()
for i in range(len(c)-1):
    d+=str(c[i])
print(d+str(c[-1]))
