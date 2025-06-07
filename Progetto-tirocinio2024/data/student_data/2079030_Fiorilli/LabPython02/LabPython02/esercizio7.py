n1=int(input('inserisci un intero: '))
n2=int(input('inserisci un altro intero:'))
n3=int(input('inserisci un altro intero: '))
print (max(n1,n2,n3))
if (n1!=max(n1,n2,n3) and n1!=min(n1,n2,n3)):
    print (n1)
elif (n2!=max(n1,n2,n3) and n2!=min(n1,n2,n3)):
    print (n2)
else:
    print (n3)
print (min(n1,n2,n3))
