finito = False
while not finito:
    s = input("Inserisci una stringa: ")
    s1 = input("Inserisci una stringa: ")
    if s[len(s)-1] == s1[0]:
        finito = True
        print(s,s1)
    
