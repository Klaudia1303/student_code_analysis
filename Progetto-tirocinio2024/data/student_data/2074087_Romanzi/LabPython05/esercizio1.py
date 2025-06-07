k=True
while k:
    s1=str(input('Prima stringa '))
    s2=str(input('Seconda stringa con stessa lunghezza della prima '))
    if len(s1)==len(s2):
        k=False
    else:
        print('Lunghezze diverse')

for i in range(len(s1)):
    print(s1[i],end='')
    print(s2[i],end='')

    
