n=1
while n<2:
      n=int(input("Inserisci numero maggiore o uguale a 2: "))

for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==n-1 or j==i or n-j-1==i):
           print("*",end="")
        else:
           print(" ",end="")
    print()
