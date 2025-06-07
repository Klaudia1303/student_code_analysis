s=input('inserisci stringa: ')
s1=input('inserisci stringa di stessa lunghezza: ')
if len(s)==len(s1):
    for i in range(len(s)):
        print(s[i],end='')
        print(s1[i],end='')
else:
    print('le due stringhe hanno lunghezza diversa')
