i =0
while i == 0:
    s = input("inserisci una stringa: ")
    print(s[0] + "" + s[len(s)-1])
    if s.isalpha() == True and s.islower() == True:
        i = i + 1
