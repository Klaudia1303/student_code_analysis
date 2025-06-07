x=input('inserire una stringa: ')
y=input('inserire un stringa di lunghezza uguale a quella precedente: ')
while len(x)!=len(y):
    x=input('inserire una stringa: ')
    y=input('inserire un stringa di lunghezza uguale a quella precedente: ')
for i in range(len(x)):
    print(x[i]+y[i],end='')

    
