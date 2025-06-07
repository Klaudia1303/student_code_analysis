n=int(input("Inserire un numero per verificare che sia primo o meno: "))
b=True;c=0;i=1
while b:
    if n%i==0:  c+=1    
    if i<n: i+=1
    else:   b=False
if c>2: print("Numero non primo")
else: print("Numero primo")
