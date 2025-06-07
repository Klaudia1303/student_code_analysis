n=""
cont=0
while(n!="*"):
    n=input("Inserisci un numero: ")
    if(n!="*"):
        n=int(n)
        if(n>=0):
            cont+=1
print(cont)
