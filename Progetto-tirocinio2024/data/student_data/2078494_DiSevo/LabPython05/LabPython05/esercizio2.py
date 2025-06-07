s = input('Inserisci una stringa: ')
n = int(input('Inserisci un numero intero positivo: '))
i=0
s1=''
while(i<len(s)):
    s1 = s1+s[i]*n
    i+=1
print(s1)
