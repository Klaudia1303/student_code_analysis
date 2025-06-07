s=str(input("Inserisci una stringa: "))
s2=str(input("Inserisci una stringa: "))
while not s[-1]==s2[0]:
    s=str(input("Inserisci una stringa: "))
    if not s2[-1]==s[0]:
        s2=str(input("Inserisci una stringa: "))
    else:
        break
print(s,"",s2)
