n1=int(input("Inserisci primo numero: "))
n2=int(input("Inserisci secondo numero: "))
lista_divisori=[]
for i in range (1,n1):
    if (n1%i==0 and n2%i != 0):
        lista_divisori.append(i)
lista_divisori.sort(reverse=True)
print(lista_divisori)

        