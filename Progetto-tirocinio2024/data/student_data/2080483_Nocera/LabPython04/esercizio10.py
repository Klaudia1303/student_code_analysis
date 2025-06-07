n1= input("inserisci una parola : ")
n2= input("inserisci una parola : ")
n3= input("inserisci una parola : ")
while (len(n1)+len(n2))!=len(n3):
    n1=n2
    n2=n3
    n3= input("inserisci una parola : ")
print(n1,n2,n3)
