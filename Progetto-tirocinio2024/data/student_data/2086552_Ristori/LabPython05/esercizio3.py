s1=str(input("Inserire una stringa:"))
s2=str(input("Inserire un'altra stringa:"))
for i in range(len(s1)):
    if s2.count(s1[i])==0:
        print(s1[i],sep='',end='')

