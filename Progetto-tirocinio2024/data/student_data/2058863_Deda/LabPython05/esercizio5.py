s=str(input('Inserisci stringa '))
n=int(input('Inserisci intero '))
t='True'
f='False'
z=''
if len(s)>=2:
    for i in range(len(s)-n):
        x=s[i]
        y=s[i+n]
        if x==y and z!=t:
            z='True'
        elif x!=y and z!=t:
            z='False'
        elif x!=y and z==t:
            z='True'
        elif x==y and z==t:
            z='True'
print(z)
