s=input('inserire una stringa: ')
z=input('inserire una stringa della stessa lunghezza: ')
if len(s)==len(z):
    for i in range(0,len(s)):
        print(str(s[i])+str(z[i]), end='')
else:
    print('input non valido')

        
