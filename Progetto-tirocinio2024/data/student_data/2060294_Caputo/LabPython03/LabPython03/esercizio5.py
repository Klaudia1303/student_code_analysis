s=input('inserisci una stringa: ')
print(s[0],s[-1])
while s.islower()==False or s.isalpha()==False:
    s=input('inserisci una stringa: ')
    print(s[0],s[-1])
print('hai inserito una stringa con tutte lettere minuscole')
