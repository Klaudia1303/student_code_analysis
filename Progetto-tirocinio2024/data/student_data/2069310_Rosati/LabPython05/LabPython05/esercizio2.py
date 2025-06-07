s=input("Inserisci una stringa: ")
n=int(input("Inserisci numero intero: "))
finale=""
for i in range(len(s)):
    finale+=s[i]*n
print(finale)
