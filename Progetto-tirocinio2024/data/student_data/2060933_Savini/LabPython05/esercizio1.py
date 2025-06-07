s=input ('inserisci una stringa ')
p=input ('inserisci una stringa ')
if len(s)==len(p):
    for i in range(len(s)):
        l=s[i]+p[i]
        print(l, end='')
    
