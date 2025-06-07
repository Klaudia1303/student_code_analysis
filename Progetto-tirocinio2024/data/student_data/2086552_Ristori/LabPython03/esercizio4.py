x=int(input("Inserire il primo numero intero:"))
y=int(input("Inserire il secondo numero intero:"))
j=0
if x==0 or y==0:
    j=1
while j<=10:
    if j==x or j==y:
        j=j+1
    else:
        print(j)
        j=j+1
  
