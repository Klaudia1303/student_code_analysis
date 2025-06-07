n1 = int(input("inserisci primo numero: "))
n2 = int(input("inserisci secondo numero: "))
i=n2
l=0
if n2>=0:
    while i>0:
        l=l+n1
        i=i-1
if n2<0:
    while i<0:
        l=l-n1
        i=i+1
print(l)
