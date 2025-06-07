n=int(input("Inserisci un numero maggiore di 0 "))
x=0
i=1
while n>i or n==i:
    if n%i==0 and n>0:
        print(i)
        i +=1
    else:
        i +=1
