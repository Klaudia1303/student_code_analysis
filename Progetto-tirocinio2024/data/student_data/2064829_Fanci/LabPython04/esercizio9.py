n = int(input("inserisci valore: "))
i=1
m0=0
m1=1
print(m1)
while i<n:
    m1=m0+m1
    print(m1)
    m0=m1-m0
    i+=1
