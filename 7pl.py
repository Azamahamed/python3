az=input()
l=[]
g=[]
for i in range(0,len(az)):
       if(i%2==0):
           l.append(az[i])
       else:
           g.append(az[i])
for i in range(0,len(az)//2):
   print(g[i],end="")
   print(l[i],end="")
