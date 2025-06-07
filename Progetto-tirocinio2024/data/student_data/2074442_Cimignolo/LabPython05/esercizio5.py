s=input('inserisci una stringa: ')
n=int(input('inserisci un numero: '))

stesso=False
car=''

for i in range(len(s)):
    if i>n:
        car=s[i-n]
    if car==s[i]:
        stesso=True
print(stesso)
    
