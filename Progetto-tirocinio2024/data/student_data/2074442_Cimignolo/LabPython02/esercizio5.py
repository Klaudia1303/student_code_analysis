s=input('inserisci anno: ')
t=int(s)
u=t%4
v=t%100
w=t%400
if u==0 and v!=0 or w==0:
    print("anno bisestile")
else:
    print("anno non bisestile")
