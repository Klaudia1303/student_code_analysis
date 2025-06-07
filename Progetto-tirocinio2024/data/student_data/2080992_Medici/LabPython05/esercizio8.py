base=int(input('inserire la base del triangolo: '))
if base%2!=0 and base>=3:
    j=(base//2)
    c=0
    for i in range(1,base//2+2):
            print(' '*j,'*'*(i+c))
            c+=1
            j-=1              
else:
    print('inserire un numero dispari maggiore o uguale a tre, riavviare il programma')
