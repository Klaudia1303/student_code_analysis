s=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero "))

for i in range(len(s)):
    for c in range(n):
        print(s[i],end='')
