s=input('inserisci una stringa: ')
n=int(input('inserisci un numero: '))
finito=False
for i in range(len(s)-n):
    if s[i]==s[i+n]:
        while not finito:
            print(True)
            finito=True
if s[i]!=s[i+n]:
    print(False)
