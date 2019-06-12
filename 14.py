gz=list(map(int,input().split()))
for j in range(gz[0]+1,gz[1]):
  if j%2 != 0:
    print(j,end=' ')
