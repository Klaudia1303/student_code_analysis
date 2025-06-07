s=str(input('Inserisci stringa '))
t=str(input('Inserisci stringa '))
u=''
x=len(s)
y=len(t)
z=len(u)
while (z+y)!=x:
    u=t
    t=s
    s=str(input('Inserisci stringa '))
    x=len(s)
    y=len(t)
    z=len(u)
print(u,t,s)
