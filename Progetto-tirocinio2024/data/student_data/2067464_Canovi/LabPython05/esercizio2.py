s = input("inserisci una stringa: ")
n = int(input("inserisci un numero intero positivo: "))
s1 = ""

for i in range(len(s)):
    s1 = s1 + s[i]*n
print(s1)
