s=str(input('inserire una stringa: '))
n=int(input('inserire un numero intero positivo: '))
j=0
for i in range(len(s)):
    while j!=len(s):
            print(s[0+j]*n,end='')
            j+=1
