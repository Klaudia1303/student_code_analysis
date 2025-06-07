t=int(input('Inserisci un valore: '))
s=input('Inserisci un carattere tra \'F\' e \'C\': ')
h=(t-32)/1.8
if (s=='C' or s=='c') and (t<=0):
    print('Stato dell\'acqua solido')
elif (s=='C' or s=='c') and (t>0 and t<100):
    print('Stato dell\'acqua liquido')
elif (s=='C' or s=='c') and (t>=100):
    print('Stato dell\'acqua gassoso')
elif (s=='F' or s=='f') and (h<=0):
    print('Stato dell\'acqua solido')
elif (s=='F' or s=='f') and (h>0 and h<100):
    print('Stato dell\'acqua liquido')
elif (s=='F' or s=='f') and (h>=100):
    print('Stato dell\'acqua gassoso')