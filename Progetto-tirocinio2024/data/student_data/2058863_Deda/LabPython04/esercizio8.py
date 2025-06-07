s=str(input('Inserisci stringa '))
t=s
x=s[0]
y=t[-1]
while x!=y:
    x=s[0]
    y=t[-1]
    if x!=y:
        t=s
        s=str(input('Inserisci stringa '))
print(t,s)
