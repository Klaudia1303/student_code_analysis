s=''
i=0
while s!=0:
    s=int(input('Inserire un numero intero o 0 per terminare: '))
    if s%3==0:
        i+=s

print(i)
