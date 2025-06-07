s=str(input('Inserisci stringa '))
z=''
for i in range(len(s)):
    x=s[i]
    y=s.count(x)
    if y>1 and z!='True':
        z='True'
    elif y>1 and z=='True':
        z='True'
    elif y<=1 and z=='True':
        z='True'
    elif y<=1 and z!='True':
        z='False'
print(z)
