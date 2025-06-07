fine=False
last=''
par=''
while not fine:
    s=input('inserisci una stringa: ')
    if last==s[0]:
        fine=True
        par=par[:-1]
    else:
        last=s[-1]
        par=par+s+' '
print(par)
