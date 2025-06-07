n1=int(input("inserisci primo numero: "))
n2=int(input("inserisci secondo numero: "))
for i in range(n1,n2):
    if i%n1==0:
        print(i)
    else:
        print("", end="")
