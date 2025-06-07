n1=int(input("Inserisci primo intero positivo: "))
n2=int(input("Inserisci secondo intero positivo: "))
div=n2//n1
if n2%n1!=0:
    for i in range(1,div+1):
        print(n1*i)
else:
    for i in range(1,div):
        print(n1*i)
    
