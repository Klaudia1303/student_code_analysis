finito=False
while not finito:
    s=input('inserisci una stringa:')
    print(s[0], s[-1])
    if s.islower()==True and s.isalpha()==True:
        finito=True
        
