s=''
i=0
while s!='*':
    s=input('Inserire un numero intero o * per terminare: ')
    if s!='*':
        if int(s)<0:
            i+=int(s)

print(i)
