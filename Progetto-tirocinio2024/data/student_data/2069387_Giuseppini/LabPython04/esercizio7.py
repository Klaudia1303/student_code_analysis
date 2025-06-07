s=input('inserisci una stringa: ')
c=0
f=0
while c<=len(s):
    x=s[c]
    if s.count(x)>f:
        f=s.count(x)
    c=c+1

print(f)
