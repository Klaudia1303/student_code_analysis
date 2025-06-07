
finito=False
while not finito:
    i=input("inserisci una stringa>> ")
    print(s[0] + s[-1])
    if s.isalpha() and s.islower():
        finito=True
