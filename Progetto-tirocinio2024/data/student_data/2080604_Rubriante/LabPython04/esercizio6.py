n=input("Inserisci un numero: ")
n1=input("Inserisci un numero: ")
i=0
prod=0
if n[0]=="-" and n1[0]=="-":
    i=int(n1[1:])
    while i>0:
        prod=prod+int(n[1:])
        i-=1
elif n[0]!="-" and n1[0]=="-":
    i=int(n1[1:])
    while i>0:
        prod=prod+int(n[0:])
        i-=1
    prod=prod-(prod+prod)
elif n[0]=="-" and n1[0]!="-":
    i=int(n1[0:])
    while i>0:
        prod=prod+int(n[1:])
        i-=1
    prod=prod-(prod+prod)
else:
    i=int(n1[0:])
    while i>0:
        prod=prod+int(n[0:])
        i-=1
print(prod)
