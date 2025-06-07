s = input("inserisci una stringa: ")
while s.isalpha() == False or s.islower() == False:
    print(s[0]+s[len(s)-1])
    s = input("inserisci una stringa: ")
print(s[0]+s[len(s)-1])


