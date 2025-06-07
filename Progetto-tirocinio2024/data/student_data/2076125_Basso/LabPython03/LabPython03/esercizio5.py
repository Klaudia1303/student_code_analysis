
d=True


while d:
    
    a=input("Inserisci stringa:\t")
    b=a.isalpha()
    c=a.islower()
    
    print(a[0],a[-1])

    if (b and c):
        d=False
