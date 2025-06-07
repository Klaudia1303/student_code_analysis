m=int(input("immetti mese in formato numerico: "))
a=int(input("immetti anno in formato numerico: "))
if m>=1 and m<=12:
    if m==12:
        print(1,a+1)
    else:
        print(m+1,a)
else:
    print("input non valido")
