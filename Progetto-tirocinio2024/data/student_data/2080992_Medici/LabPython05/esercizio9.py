lato=int(input('inserire il lato del quadrato: '))
if lato%2!=0 and lato>=3:
    if lato==3:
        print('*'*3)
        print('*','*')
        print('*'*3)
    else:
        print('*'*lato)
        for i in range(1,(lato//2)+2):
            j=lato-4
            print('*',' '*j,'*')
        print('*'*lato)
else:
    print('inserire un numero dispari maggiore o uguale a tre, riavviare il programma')
