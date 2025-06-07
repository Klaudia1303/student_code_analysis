s = input("Inserisci almeno due caratteri: ")
n = int(input("Inserisci un numero intero positivo: "))

success = False

for i in range(len(s)-n):
    if s[i] == s[i+n]:
        success = True
        break

print(success)
