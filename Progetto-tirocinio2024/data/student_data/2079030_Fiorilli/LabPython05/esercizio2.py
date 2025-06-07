s=input('inserisci una stringa: ')
n=-1
while n<=0:
    n=int(input('inserisci un intero positivo: '))
for i in range (len(s)):
    print (s[i]*n,end='')
