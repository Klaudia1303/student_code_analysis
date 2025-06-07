s=input('inserisci una stringa ')
n=input('inserisci una stringa avente la stessa lunghezza della prima ')
d=''
if len(s)==len(n):
    for i in range(len(s)):
        d=d+s[i]+n[i]
    print(d)
else:
    print('le due stringhe non hanno la stessa lunghezza')
        
