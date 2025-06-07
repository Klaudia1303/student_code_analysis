n='ciao'
d=0
while n!=0:
    n=input("Inserire un numero intero: ")
    n=int(n)
    if n%3==0:
        d+=1
    
print(d)
