n1=int(input('inserisci un intero: '))
n2=int(input('inserisci un intero: '))
while n1<=0 or n2<=0:
    n1=int(input('inserisci un intero: '))
    n2=int(input('inserisci un intero: '))
for i in range(1,n2):
    if i%n1==0:
        print(i)
