s=str(input("Inserisci una stringa>> "))
n=int(input("Inserisci un numero intero>> "))
i=0
for i in range(len(s)):
    print(s[i]*n,end="")
    i=i+1
