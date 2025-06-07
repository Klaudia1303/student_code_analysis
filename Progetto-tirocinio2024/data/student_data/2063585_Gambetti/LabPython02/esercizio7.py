x=int(input('inserisci un numero: '))
y=int(input('inserisci un numero: '))
z=int(input('inserisci un numero: '))
if int(x)>int(y)>int(z):
    print(x)
    print(y)
    print(z)
elif int(x)>int(z)>int(y):
    print(x)
    print(z)
    print(y)
elif int(y)>int(x)>int(z):
    print(y)
    print(x)
    print(z)
elif int(y)>int(z)>int(x):
    print(y)
    print(z)
    print(x)
elif int(z)>int(x)>int(y):
    print(z)
    print(x)
    print(y)
elif int(z)>int(y)>int(x):
    print(z)
    print(y)
    print(x)
