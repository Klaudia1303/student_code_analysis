b=int(input('inserisci la base del triangolo isoscele (dispari, maggiore o uguale a 3): '))
for i in range(b+1):
    if i%2!=0:
        print(((b-i)//2)*' ','*'*i)
