s1=str(input('inserire una stringa: '))
s2=str(input('inserire una stringa: '))
j=0
if len(s1)==len(s2):
    for i in range(len(s1)):
        while j!=len(s1):
            print(s1[0+j]+s2[0+j], end='')
            j+=1
else:
    print('bisogna inserire due stringhe della stessa lunghezza, riavviare il programma')
    
