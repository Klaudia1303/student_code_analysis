s=input('inserisci una stringa: ')
ultima=''
prima=s[0]
while ultima!=prima:
    a=s
    ultima=s[len(s)-1]
    s=input('inserisci una stringa: ')
    prima=s[0]
print(a,s)
