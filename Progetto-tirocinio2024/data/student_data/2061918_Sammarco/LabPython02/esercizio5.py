A= input("inserisci un anno")
A= int(A)
if A%4 ==0 and A%100 != 0 or A%400 == 0:
    print("anno bisestile")
else:
    print("anno non bisestile")    
