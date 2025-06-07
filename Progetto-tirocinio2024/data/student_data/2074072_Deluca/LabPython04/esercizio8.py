s=input("inserisci prima stringa ")
P="\n"
corretto=False
while not corretto:
    p=input("inserisci stringa ")
    if p[len(p)-1]!=s[0]:
        corretto=False
        s=p
    else :
        corretto=True
print(p+" "+s)
    
    
