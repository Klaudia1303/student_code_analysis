s=input('inserire un numero intero (* per terminare): ')
c=0

while s!='*':
    if int(s)>=0:
        c+=1
    s=input('inserire un numero intero (* per terminare): ')
print(c)
