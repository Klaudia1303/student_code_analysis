n1 = int(input("Inserisci il numero: "))
n2 = int(input("Inserisci il numero: "))
neg = False
if n1<0:
    n1 = abs(n1)
    neg = True
if n2<0:
    n2 = abs(n2)
    if neg:
        neg = False
    else:
        neg = True
tot = 0
while n1>0:
    tot += n2
    n1 -= 1
if neg:
    tot *= -1
print(tot)
    