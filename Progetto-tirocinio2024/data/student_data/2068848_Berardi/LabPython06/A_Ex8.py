s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
n=int(input('inserisci un passo: '))
x=len(s1)
minimo=len(s1)
for i in range(x):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            if i<minimo:
                minimo=i
            if i<=minimo+n:
                print(s2[j],end="")