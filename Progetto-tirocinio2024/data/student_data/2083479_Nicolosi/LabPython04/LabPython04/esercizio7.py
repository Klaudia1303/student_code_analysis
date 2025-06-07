s=input('Inserisci una stringa: ')
n=0
x=s.count(s[n])
while x<2:
    x=s.count(s[n])
    n+=1
print(s[n])