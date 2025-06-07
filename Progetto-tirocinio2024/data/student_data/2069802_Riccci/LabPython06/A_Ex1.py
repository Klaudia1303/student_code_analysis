divisori = list()
n1 = int(input("Inserisici numero intero maggiore edi 0 --> "))
n2 = int(input("Inserisici numero intero maggiore edi 0 --> "))
if n1>=n2:
    max_=n1
    min_=n2
else:
    max_=n2
    min_=n1
for i in range(2,max_+1):
    if max_%i==0 and min_%i!=0:
        divisori.append(i)
a=len(divisori)
for i in range(1,a+1):
    print(divisori[a-i])
