n=int(input())
for i in range(1,n+1):
 if i!=1 and i!=n:
    for k in range(n-i):
        print(" ",end="")
    print("*",end="")
    for k1 in range(i+i-3):
        print(" ",end="")
    print("*")
 elif i==1 and i!=n:
    for k1 in range(n-1):
        print(" ",end="")
    print("*")
 elif i==n:
  for l in range(n):
    print("*",end=" ")
 
