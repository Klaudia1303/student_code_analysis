n1 = int(input('inserisci n1: '))
n2 = int(input('inserisci n2: '))
n3 = int(input('inserisci n3: '))
if n1<n2<n3:
    print(n3,n2,n1)
if n1<n3<n2:
    print(n2,n3,n1)
if n2<n1<n3:
    print(n3,n1,n2)
if n2<n3<n1:
    print(n1,n3,n2)
if n3<n2<n1:
    print(n1,n2,n3)
if n3<n1<n2:
    print(n2,n1,n3)
    
