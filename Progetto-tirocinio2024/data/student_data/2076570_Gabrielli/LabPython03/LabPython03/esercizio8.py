s=input('inserisci una stringa palindroma: ')
a=s[:]
b=s[::-1]
while s:
    if a==b:
        print('la stringa s è lunga:',len(s))
    else:
        print('stringa non palindroma')
        s=input('inseriusci una stringa palindroma')
