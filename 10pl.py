az=input()
az=az.split(" ")
gg=az[0]
hh=az[1]
for i in range(0,len(gg)):
        c=0
        if(gg[i]!=hh[i]):
             c=c+1
if(c==1):
     print("yes")
else:
     print("no")
