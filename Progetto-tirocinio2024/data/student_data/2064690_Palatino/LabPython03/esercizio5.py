s=input('inserisci una stringa: ')
while not s.isalpha() or not s.islower():
    print(s[0],s[-1])
    s=input('inserisci una stringa: ')
print(s[0],s[-1])
 
