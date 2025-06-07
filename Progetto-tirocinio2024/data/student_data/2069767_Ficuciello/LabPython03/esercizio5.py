finito = False
while not finito:
    s=input('Inserire una stringa:' )
    print(s[0],s[-1])
    if (s.isalpha() and s.islower())== True:
        finito = True
    

