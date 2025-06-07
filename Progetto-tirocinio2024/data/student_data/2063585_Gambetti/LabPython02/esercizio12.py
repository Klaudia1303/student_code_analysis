t=int(input('inserisci una temperatura: '))
s=input('inserisci la scala di temperatura usando C per i celsius e F per i Fahrenheit: ')
x=(t-32)/1.8
if s=='C':
    if int(t)<=0:
        print('è solida')
    elif int(t)>0 and int(t)<100:
        print('è liquida')
    elif int(t)>=100:
        print('è gassosa')
elif s=='F':
    if int(x)<=0:
          print('è solida')
    elif int(x)>0 and int(x)<100:
        print('è liquida')
    elif int(x)>=100:
        print('è gassosa')
        
    
