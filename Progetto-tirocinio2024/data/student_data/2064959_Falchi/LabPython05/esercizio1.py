s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")

sFinale = "" 

if len(s1) != len(s2):
    print("ERRORE! Le due stringhe devono avere la stessa lunghezza.")
    exit()

for i in range(len(s1)):
    sFinale += (s1[i] + s2[i])

print(sFinale)
