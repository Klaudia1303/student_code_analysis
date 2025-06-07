termina=False
while not termina:
    s=input("Immetti una stringa: ")
    print(s[0]+s[-1])
    if s.isalpha() and s.islower():
        termina=True
