s='a'
i=1
j=0

while(s!='*'):
    s=input("Inserisci un numero intero: ")
    if(s!='*'):
        s=int(s)
        if(s>0):
            j+=1

print(j)

        
