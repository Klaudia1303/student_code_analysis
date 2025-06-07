x=input('inserisci stringa')
y=''
z=''
while len(z)+len(y)!=len(x):
    z=y
    y=x
    x=input('inserisci stringa')
print (z+' '+y+' '+x)
