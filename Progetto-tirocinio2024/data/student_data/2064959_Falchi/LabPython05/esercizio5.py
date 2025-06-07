from re import S


s = input("Inserire una stringa di almeno due caratteri: ")
n = int(input("Inserire un numero intero positivo: "))

if len(s) < 2 or len(s) < n:
    print("ERRORE! La stringa è troppo corta!")
    exit()

for i in range(len(s)-n):
    if s[i] == s[i+n]:
        print(True) #True viene stampato se ci sono lettere uguali a distanza di n posizioni.
        exit()

print(False) #False viene stampato se non ci sono lettere uguali a distanza di n posizioni.