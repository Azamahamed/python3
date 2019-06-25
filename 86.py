f=input()
az=""
for a in f:
  if a not in az:
    az=az+a
if(f==az):
  print("Yes")
else:
  print("No")
