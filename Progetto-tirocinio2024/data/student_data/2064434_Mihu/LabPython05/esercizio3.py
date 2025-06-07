s1=str(input("inserisci stringa: "))
s2=str(input("inserisci stringa: "))
i=0
y=0
corretto=False
while i<len(s1):
    while y<len(s2) and corretto==False:
        if s1[i]!=s2[y]:
            corretto=False
            y=y+1
        else:
            corretto=True
            y=0
    if corretto==False:
        print(s1[i],end=(""))
    i=i+1
    y=0
    corretto=False
    
