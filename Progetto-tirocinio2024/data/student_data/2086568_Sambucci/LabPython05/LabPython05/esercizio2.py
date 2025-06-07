s=input('Inserire una stringa: ')
n=int(input('Inserire numero intero: '))
sripetuta=''
for i in range(len(s)):
    sripetuta=sripetuta+s[i]*n
print(sripetuta)
