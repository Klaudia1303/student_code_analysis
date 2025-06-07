s=input("Inserisci una stringa : ")
n=int(input("Inserisci un numero intero : "))
a=""
for i in range(len(s)):
    a+=s[i]*n
print(a)