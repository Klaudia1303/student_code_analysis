
n=int(input("Inserisci intero maggiore di 0:\t"))
a=1
b=0

while a<= n:
    if n%a==0:
        b=b+1
    a=a+1
if b==2:
    print("numero primo")
else:
    print("numero non primo")
