n1=int(input('inserire un numero intero: '))
n2=int(input('inserire un numero intero: '))
i=1
c=0
nt=0
for c in range(n2):
    nt=n1*i
    if nt<n2:
        print(nt)
        c+=1
        i+=1
    else:
        c+=1
        i+=1
        
