x=input("inserici un intero (* per terminare): ")
somma=0
while x!='0':
    if int(x)%3==0:
        somma=int(somma)+int(x)
        x=input('inserici un intero (* per terminare): ')
    else:
        x=input('inserici un intero (* per terminare): ')
print(somma)
    
