s=input('Inserire una stringa: ')
t=input('Inserire una stringa: ')
z=input('Inserire una stringa: ')
while len(s)+len(t)!=len(z):
    s=t
    t=z
    z=input('Inserire una stringa: ')
print(s,t,z)

    
    
