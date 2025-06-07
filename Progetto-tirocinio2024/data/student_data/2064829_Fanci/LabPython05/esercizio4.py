n1 = int(input("inserisci primo intero: "))
n2 = int(input("inserisci secondo intero: "))
for i in range(1,n2):
    n=n1*i
    if n>=n2:
        break
    else:
        print(n)

