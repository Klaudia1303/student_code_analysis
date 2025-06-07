x=input("inserici un intero (* per terminare): ")
somma=0
while x!='*':
    if int(x)>=0:
        somma=somma+1
        x=input('inserici un intero (* per terminare): ')
    else:
        x=input('inserici un intero (* per terminare): ')
print(somma)
    
