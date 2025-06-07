s1=input('Inserire una stringa:')
s2=input('Inserire una stringa della stessa lunghezza della prima:')
if len(s1)==len(s2):
    x=''
    for i in range (len(s1)):
        x+=s1[i]
        x+=s2[i]
    print(x)
else:
    print('Le due stringhe hanno lunghezza differente')
