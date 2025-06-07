n1=int(input("Inserisci il primo intero"))
n2=int(input("Inserisci il secondo intero"))
i=0
molt=0
if n1==0 or n2==0:
    print(0)
while i!=n2:
    molt+=n1
    i+=1
print(molt)
