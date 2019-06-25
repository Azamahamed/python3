import math
hd,y=input().split()
x=int(hd)
y=int(y)
z=(math.gcd(x,y))
print((x*y)//z)
