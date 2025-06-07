#57
s=(input("inserisci una stringa: "))
i=0
corretto=False

while i<len(s) and corretto==False:
    x=s.rfind(s[i])
    if x!=-1:
        corretto=True
        print(x)
    else: i=i+1
