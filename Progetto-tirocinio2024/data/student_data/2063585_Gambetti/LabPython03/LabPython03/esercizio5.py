s=input('inserisci una stringa: ')
finito=False
while not finito:
    if s.islower()!=True or s.isalpha()!=True or (s.islower()!=True and a.isalpha()!=True):
        n=len(s)
        print(s[:1]+s[n-1:n])
        s=input('inserisci una stringa: ')
    else:
        n=len(s)
        print(s[:1]+s[n-1:n])
        finito=True
