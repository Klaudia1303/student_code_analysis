m = int(input('inserisci mese: '))
a = int(input('inserisci anno: '))
if m>=1 and m<12:
    print(m+1)
    print(a)
if m==12:
    print((m+1)%12)
    print((m+1)%12+a)
       

