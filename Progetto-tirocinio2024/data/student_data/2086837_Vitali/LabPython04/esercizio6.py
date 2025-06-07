n1=int(input("Inserisci 1' numero intero: "))
n2=int(input("Inserisci 2' numeor intero: "))
somm=0
if (n1>0 and n2<0) or (n1<0 and n2>0):
    if n1>n2:
        for i in range(n1):
            somm +=n2
    else:
        for i in range(n2):
            somm +=n1
if n1<0 and n2<0:
    n1=-n1
    n2=-n2
if n1>0 and n2>0:
    if n1>n2:
        for i in range(n2):
            somm +=n1
    else:
        for i in range(n1):
            somm +=n2
print(somm)
    
