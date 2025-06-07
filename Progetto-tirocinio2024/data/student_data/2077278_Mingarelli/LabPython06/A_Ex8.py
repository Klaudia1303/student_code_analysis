s=input('iserisci una stringa ')
l=input('inserisci una seconda sringa ')
n=int(input('inserisci un numero intero '))
new=''
for i in range(len(s)):
    if l.find(s[i])!=-1:
        if l.find(s[i])-i<=n and i-l.find(s[i])<=n:
            new=new+s[i]
print(new)
