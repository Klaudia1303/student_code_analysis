s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")

sFinale = ""

for i in range(len(s1)):
    if not s1[i] in s2:
        sFinale += s1[i]

print(sFinale)