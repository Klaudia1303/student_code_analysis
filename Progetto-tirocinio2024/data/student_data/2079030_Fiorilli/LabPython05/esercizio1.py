s=''
t=' '
while len(s)!=len(t):
    s=input('inserisci una stringa: ')
    t=input('inserisci una strnga lunga come la precedente: ')
for i in range (len(s)):
    print (s[i],t[i],sep='',end='')
