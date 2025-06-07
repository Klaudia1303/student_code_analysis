n1 = int (input ('Inserisci il primo numero: '))
n2 = int (input ('Inserisci il secondo numero: '))
volte = n2//n1
i=0
while i<volte:
    i=i+1
    n3=n1*i
    if n3<n2 :
        print (n3)
    else:
        break
