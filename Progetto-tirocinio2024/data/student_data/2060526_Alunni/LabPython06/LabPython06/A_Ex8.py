x=(input('inserisci una stringa:  '))
y=(input('inserisci una stringa:  '))
n=int(input('inserisci un numero: '))
s=str()
f=0
for i in range(0,len(x)):
    j=i+n
    f=i-n
    if x[i]in y:
        l=i
        if y.find(x[i]) in range(f,j):
            s=(s+x[i])
print(s)
