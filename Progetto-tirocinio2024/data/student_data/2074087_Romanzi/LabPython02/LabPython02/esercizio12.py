t=float(input('Temperatura '))
s=str(input('Scala '))
if ord(s)!=70 and ord(s)!=67:
    print('Scala inserita non valida')
else:
    if ord(s)==70:
        c=(t-32)/1.8
        if c<=0:
            print('Gassosa')
        elif c>=100:
            print('Solida')
        else:
            print('Liquida')
    else:
        if t<=0:
            print('Gassosa')
        elif t>=100:
            print('Solida')
        else:
            print('Liquida')
        
        
                  
    
