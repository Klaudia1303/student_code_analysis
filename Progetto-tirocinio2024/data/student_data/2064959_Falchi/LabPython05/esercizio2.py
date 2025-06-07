s = input("Inserire una stringa: ")
n = int(input("Inserire un valore: "))

sFinale = ""

for i in range(len(s)):
    sFinale += s[i]*n

print(sFinale)