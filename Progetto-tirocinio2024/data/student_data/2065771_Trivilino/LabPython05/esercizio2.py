s=input('Inserire una stringa: ')
n=int(input('Inserire un intero positivo: '))
f=''
for i in range(0,len(s)):
    f+=s[i:i+1]*n
print(f)
