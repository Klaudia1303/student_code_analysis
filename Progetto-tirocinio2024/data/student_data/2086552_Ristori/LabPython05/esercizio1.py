s1=str(input("Inserire una stringa:"))
s2=str(input("Inserire un'altra stringa con lo stesso numero di caratteri della precedente:"))
for i in range(len(s2)):
    print(s1[i],s2[i],sep='',end='')

