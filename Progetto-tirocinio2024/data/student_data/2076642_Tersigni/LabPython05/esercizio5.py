s=input("inserisci una stringa")
n=int(input("inserisci un intero"))
i=0
corretto=True
while (i+n)<len(s):
    if s[1]==s[i+n] and corretto:
        print(True)
        corretto=False
    i+=1
if corretto==True:
    print(False)
