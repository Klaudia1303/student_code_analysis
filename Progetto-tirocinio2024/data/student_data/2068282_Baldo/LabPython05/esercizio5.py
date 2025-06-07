s = input("inserisci una stringa con almeno 2 caratteri: ")
n = int(input("inserisci un intero positivo: "))
k = False

for i in range(len(s)-n):
    if s[i] == s[i + n]:
        k = True
print(k)
    
