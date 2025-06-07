s=input("inserisci stringa: ")
n=int(input("inserisci un numero intero: "))
i=0
for numero in range(len(s)):
    lettera=s[i]*n
    print(lettera, end=(""))
    i=i+1
