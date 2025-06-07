a = input('inserisci anno :')
m = input('inserisci mese :')
a = int(a)
m = int(m)
if m >= 1 and m < 12:
     
    print (m+1, a)

elif  m == 12: 
        print(m+1, a+1)
else:
    print('input non valido')
    
    
