t=int(input('Inserire un valore intero corrispondente ad una temperatura:' ))
if 30<t:
    print(t, 'molto caldo')
elif 20<t<=30:
    print(t, 'caldo')
elif 10<t<=20:
    print(t, 'gradevole')
elif t<=10:
    print(t, 'freddo')
