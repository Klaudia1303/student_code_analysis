s = input("Inserisici stringa -->")
n = int(input("Inserisci numero intero --> "))
stringa_finale=""
for i in range(len(s)):
    stringa_finale+=s[i]*n
print(stringa_finale)
