n1 = input('inserisci numero :')
n1 = int(n1)
n2 = input('inserisci numero :')
n2 = int(n2)
n3 = input('inserisci numero :')
n3 = int(n3)
if n1 < n2 and n2 < n3:
    print(n3 , n2 , n1)
    
elif n2 < n1 and n1 < n3 :
    print(n3 , n1 , n2)

elif n3 < n2 and n2 < n1:
    print(n1, n2 , n3)

elif n3 < n1 and n1 < n2 :
    print(n2, n1 , n3)
