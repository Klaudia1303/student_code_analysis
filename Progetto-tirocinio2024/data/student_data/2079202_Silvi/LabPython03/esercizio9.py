print("questo programma verifica se un numero è primo\n")

n=int(input("inserire un numero:"))
primo=True
for i in range (2,n):

    if n%i==0 and i!=1 and i!=n:

        primo=False

if primo:
    print("numero primo")
else:
    print("numero non primo")
