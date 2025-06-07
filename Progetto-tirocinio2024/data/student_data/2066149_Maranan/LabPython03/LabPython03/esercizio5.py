s = input('Inserisci una stringa quasiasi oppure una composta da soli caratteri minuscoli \
per terminare: ')

i = 1

while i != 0:
    print (s[0]+s[-1])
    s = input('Inserisci un\'altra stringa quasiasi oppure una composta da soli caratteri minuscoli \
per terminare: ')

    if s.isalpha() and s.islower():
        print (s[0]+s[-1])
        i = 0
        
        
