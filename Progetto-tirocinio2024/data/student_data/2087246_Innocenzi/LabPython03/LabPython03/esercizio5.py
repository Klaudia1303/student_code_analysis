s=input("Inserisci una stringa: ")
print(s[0] + s[-1])

while not(s.isalpha() is True and s.islower() is True):
        s=input("Inserisci una stringa: ")
        print(s[0] + s[-1])


