a=int(input('inserisci un anno'))
if a!=0 and a%4==0 and a%100!=0 or (a!=0 and a%100==0 and a%400==0):
    print("l'anno è bisestile")
else:
    print("anno non bisestile")
