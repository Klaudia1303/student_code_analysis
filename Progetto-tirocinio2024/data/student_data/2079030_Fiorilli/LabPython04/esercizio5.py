n=int(input('inserisci un valore intero maggiore o uguale a zero: '))
while n<0:
  n=int(input('inserisci un valore intero maggiore o uguale a zero: '))  
f=1
c=2
while c<=n:
    f=f*c
    c+=1
print (f)
