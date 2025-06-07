s = input("inserisci una stringa: di almeno due caratteri ")
n = int(input("inserisci un numero intero positivo: "))
a = 0

for i in range((len(s) - n)):
    if s[i] == s[i + n]:
        a = a + 1
if a == 0:
    print("False")
else:   print("True")


