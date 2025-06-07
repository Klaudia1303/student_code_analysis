s=input("Inserisci una stringa: ")
while s=="":
    s=input("Inserisci una stringa: ")
lun=len(s)
mix=0
ris=""
while lun>0:
    if s.count(s[lun-1])>mix:
        mix=s.count(s[lun-1])
        ris=s[lun-1]
    elif s.count(s[lun-1])==mix:
        if s.rfind(ris)<s.rfind(s[lun-1]):
            ris=s[lun-1]
    lun-=1
print(ris)
