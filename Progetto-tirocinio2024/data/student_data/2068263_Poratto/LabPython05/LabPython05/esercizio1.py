a=str(input('inserire una stringa '))
b=str(input('inserire una stringa avente la stessa lunghezza della prima '))
for i in  range(len(a)):
    k=a[i]+b[i]
    print(k,end='')
