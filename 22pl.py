num1,num2=map(int,input().split())
al=[]
for i in range (1,num2+1):
  if (num1%i==0 and num2%i==0):
    al.append(i)
print(max(al))
